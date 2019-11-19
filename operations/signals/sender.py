from django.db.models.signals import post_save
from django.dispatch import receiver
from trainingvenv.operations.models import RiskDetail
from django.core.mail import send_mail


@receiver(post_save, sender=RiskDetail)
def my_handler(instance, created, **kwargs):
    if created:
        print(" sender email processing ")
        send_mail('Hazard Report ',
                  'A Hazard has been registered in the in the system. '
                  'Please logon http://127.0.0.1:8000 to view this Report',
                  'tipsoff@nhszim.com', ['mukwazhi@gmail.com', 'bmukwazhi@nhszim.com'])
        print(" email send ")