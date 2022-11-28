from datetime import timedelta

import requests
from .models import Subscription
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


def send_forget_password_mail(email, token):
    subject = "Your forget password link"
    message = f"Hi , clik on the link to reset your password {settings.DOMAIN}/{token}/"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def upgrade_reminder_mail(email, user):
    # use mailgun scheduled email api
    if Subscription.objects.filter(user=user).exists():
        qs = Subscription.objects.get(user=user)
        print(qs.valid_upto)
        if qs.valid_upto - timezone.now() == timedelta(days=10):
            subject = "Your Plan is Expireing Soon..!"
            message = "Your upgrade plan about to end within 10 days..!. Please Renew Your Plan. Thank You "
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)


def send_scheduled_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        data={
            "from": "Excited User <YOU@YOUR_DOMAIN_NAME>",
            "to": "bar@example.com",
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!",
            "o:deliverytime": "Fri, 25 Oct 2011 23:10:10 -0000",
        },
    )
