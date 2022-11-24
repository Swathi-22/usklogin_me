from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail

from .models import Subscription
from datetime import datetime
from django.utils import timezone



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
    print(qs.valid_upto)
    if qs.valid_upto - timezone.now() == timedelta(days=10):
        subject = "Your Plan is Expireing Soon..!"
        message = "Your upgrade plan about to end within 10 days..!. Please Renew Your Plan. Thank You "
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    else:
        pass
