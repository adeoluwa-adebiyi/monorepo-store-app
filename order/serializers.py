from rest_framework import serializers


        # payload = {
        #     "cardno": card_num,
        #     "cvv": cvv,
        #     "expirymonth": exp_month,
        #     "expiryyear": exp_year,
        #     "amount": amount,
        #     "email": email,
        #     "phonenumber": phone,
        #     "firstname": firstname ,
        #     "lastname": lastname,
        #     "IP": ip
        #     "txRef": txn_id
        # }

class TrxJobSerializer(serializers.Serializer):
    cardno = serializers.CharField(required=True)
    cvv = serializers.CharField(required=True)
    expirymonth = serializers.CharField(required=True)
    expiryyear = serializers.CharField(required=True)
    amount = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    phonenumber = serializers.CharField(required=True)
    firstname = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    trxjob_id = serializers.IntegerField(required=False)


class OtpSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True)