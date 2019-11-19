from .models import TrainingRecord,Trainer,Employee,Course,Department,JobTitle,Section
from datetime import date
from django.core.mail import send_mail


def autoEmail():


    # Red Zone
    # The count of all the expired employees
    expired_info = TrainingRecord.objects.filter(training_expiry__lt=date.today()).exclude(archive=1).count()

    # Orange Zone
    # the count of all the employees whose courses will expire within 0 to 60 days
    expired_inf = TrainingRecord.objects.filter(training_expiry__gt=date.today()).exclude(archive=1)
    count = 0
    for e in expired_inf:
        diff = e.training_expiry - date.today()
        if diff.days < 60:
            print(e.training_expiry - date.today())
            count += 1
    print(count)

    # send email
    send_mail(
        'training Status',
        str(expired_info) + ' Employees have expired\n'+ str(count)+' Employees are within the Orange Zone ',
        'matrix@example.com',
        ['mukwazhi@gmail.com'],
        fail_silently=False,
    )