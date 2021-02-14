from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from .models import Job, TransactionJob


@receiver(post_save, sender=Job)
def job_status_event_handler(job):

    if isinstance(job, TransactionJob):

        if job.status == "SATISFIED":
            order = job.order
            order.status = "SATISFIED"
            order.save()
        elif job.status == "FAILED:
            order = job.order
            order.status = "FAILED"
            order.save()
    else:
        pass
