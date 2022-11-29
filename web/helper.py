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
        qs.valid_upto - timezone.now() == timedelta(days=10)


def send_scheduled_message(data):
    DOMAIN_NAME = "sandboxd8904f8fd59b40eab3139d5031e4dcaf.mailgun.org"
    API_KEY = "913731f1be6bac9b41e2d3f69fdf2656-69210cfc-8ba19ad2"
    FROM_EMAIL = settings.MAILGUN_FROM_EMAIL
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", API_KEY),
        data={"from": FROM_EMAIL, "to": data.get("email"), "subject": data.get("subject"), "text": data.get("message"), "o:deliverytime": data.get("delivery_time")},
    )


# calling the function
send_scheduled_message(
    {
        "email": ["contact@gedexo.com"],
        "subject": "Your Plan is Expiriing Soon..!",
        "message": "Your plan is about to end in 10 days..!. Please Renew Your Plan. Thank You",
        "delivery_time": "Fri, 25 Oct 2011 23:10:10 -0000",
    }
)
