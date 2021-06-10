from django.shortcuts import render, redirect
from django.views.generic import View
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.db.transaction import atomic
from uuid import uuid4
from modules.services.checkout.checkout_service import CheckoutService
from modules.services.order.order_service import OrderService
from modules.exceptions.checkout_exceptions import InsufficientProductQuantityError,\
     DuplicateTransactionPaymentException
from kafka import KafkaProducer
from .producers import redis, TOPIC_ID, SERVERS, kafka_producer
from .models import TransactionJob, Order
from .serializers import TrxJobSerializer, OtpSerializer
import json
from django.urls import reverse


class CheckoutCartView(View):

    def get(self, request: HttpRequest):
        template_name = "card_payment_page.html"
        try:
            with atomic():
                checkout_id = CheckoutService().checkout(request.session["cart"])
                order: Order = OrderService().create_order(checkout_id=checkout_id)
                context = dict()
                context["order_id"] = order.id
                context["amount"] = order.total_price
                request.session["cart"] = []
                request.session["cart_total_items"] = 0
                request.session["cart_total_rpice"] = 0
                return render(request, template_name, context)
        except Exception as e:

            if isinstance(e, InsufficientProductQuantityError):
                return HttpResponse(str(e))
            print(e)
            return HttpResponse("Checkout Failed")


class PayTransactionView(View):

    def post(self, request: HttpRequest, order_id: int):
        trx_data = TrxJobSerializer(data=request.POST)
        trx_job = None
        if trx_data.is_valid(raise_exception=True):

            trx_set=TransactionJob.objects.filter(order__id=order_id)

            trx_job = None

            if trx_set.exists():
                trx = trx_set.last()

                if trx.status == "SATISFIED":
                    raise DuplicateTransactionPaymentException("Duplicate transaction")

                elif trx.status == "PENDING":
                    trx_job = TransactionJob.objects.get(order__id=order_id)
            else:
                trx_job = TransactionJob.objects.create(order=Order.objects.get(id=order_id), payment_data=trx_data.validated_data)

            # producer = redis
            # producer.publish("payment_request", json.dumps({**trx_data.validated_data, "trxjob_id": trx_job.id}))

            producer = kafka_producer
            producer.publish("payment_request", json.dumps({**trx_data.validated_data, "trxjob_id": trx_job.id}))

            pubsub = producer.pubsub()
            event = f"payment_otp#{trx_job.id}"
            pubsub.subscribe(event)

            for message in pubsub.listen():
                if message.get("type") == "message":
                    print(message)
                    pubsub.unsubscribe(event)
                    break
            return redirect(f"/order/authorize/{trx_job.id}")


class AuthorizeOtpView(View):

    def get(self, request: HttpRequest, trxjob_id=None):

        template_name = "otp_form.html"

        context = dict()
        context["trx_id"] = trxjob_id

        return render(request, template_name, context)

    def post(self, request, trxjob_id):

        if trxjob_id == None:
            return HttpResponse("Payment Authorization failed: Invalid URL")

        trx_job = TransactionJob.objects.filter(id=trxjob_id)

        if not trx_job.exists():
            return HttpResponse("Payment Authorization failed: Invalid Transaction")

        trx_job = trx_job.last()

        response = None
        data  = OtpSerializer(data=request.POST)
        if data.is_valid(raise_exception=True):
            producer = redis
            producer.publish("payment_authorized", json.dumps({**data.validated_data, "trxjob_id": trxjob_id}))
            pubsub = producer.pubsub()
            event = f"payment_status#{trxjob_id}"
            pubsub.subscribe(event)

            for message in pubsub.listen():
                if message.get("type") == "message":
                    print("RESPONSE")
                    print(message)
                    response = message.get("data")
                    pubsub.unsubscribe(event)
                    break


            response = json.loads(response)

            print(response)

            if response["success"] == True:
                
                trx_job.status = "SATISFIED"
                trx_job.save()
                return HttpResponse("Payment successful")
            else:
                trx_job.status = "FAILED"
                trx_job.save()
                return HttpResponse("Payment failed")

        pass

