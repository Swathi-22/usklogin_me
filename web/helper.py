from django.conf import settings
from django.core.mail import send_mail

from .models import Subscription
from datetime import datetime


def send_forget_password_mail(email, token):
    subject = "Your forget password link"
    message = f"Hi , clik on the link to reset your password http://usklogin.geany.website/{token}/"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def upgrade_reminder_mail(email, user):
    today=datetime.now()
    qs=Subscription.objects.get(user=user)
    val=""
    for sub in qs:
        val=sub.valid_upto
    if val-today == 10:
        return status==True
    else:
        return status==False

    if status:
        subject = "Your Plan is Expireing Soon..!"
        message = "Your upgrade plan about to end within 10 days..! "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    else:
        pass
