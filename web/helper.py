import requests
from django.conf import settings


def upgrade_reminder_mail(email, user):
    # use mailgun scheduled email api
    # if Subscription.objects.filter(user=user).exists():
    #     qs = Subscription.objects.get(user=user)
    pass


def send_scheduled_message(data):
    return requests.post(
        f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN_NAME}/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": settings.MAILGUN_FROM_EMAIL,
            "to": data.get("email"),
            "subject": data.get("subject"),
            "text": data.get("message"),
            "o:deliverytime": data.get("delivery_time"),
        },
    )


# calling the function
# send_scheduled_message(
#     {
#         "email": ["contact@gedexo.com"],
#         "subject": "Your Plan is Expiring Soon..!",
#         "message": "Your plan is about to end in 10 days..!. Please Renew Your Plan. Thank You",
#         "delivery_time": "Fri, 25 Oct 2011 23:10:10 -0000",
#     }
# )
