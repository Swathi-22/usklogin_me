from notification.models import BroadcastNotification
from services.models import BrandingImage

from django.conf import settings


def main_context(request):
    if request.user.is_authenticated:
        if request.user.session_set.all().count() > settings.MAX_DEVICE_SESSIONS:
            request.user.session_set.filter(pk__in=request.user.session_set.order_by("-last_activity").values_list("pk")[settings.MAX_DEVICE_SESSIONS :]).delete()
    branding_image = BrandingImage.objects.all()
    return {
        "branding_image": branding_image,
        "ONESIGNAL_APP_ID": settings.ONESIGNAL_APP_ID,
        "ONESIGNAL_SAFARI_WEB_ID": settings.ONESIGNAL_SAFARI_WEB_ID,
        "RAZOR_PAY_KEY": settings.RAZOR_PAY_KEY,
        "RAZOR_PAY_SECRET": settings.RAZOR_PAY_SECRET,
    }


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {"notifications": allnotifications}
