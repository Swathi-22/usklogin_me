from accounts.models import User
from django.conf import settings

from notification.models import BroadcastNotification
from services.models import BrandingImage





def main_context(request):

    if request.user.is_authenticated:
        if request.user.session_set.all().count() > settings.MAX_DEVICE_SESSIONS:
            request.user.session_set.all().order_by('-last_activity')[:settings.MAX_DEVICE_SESSIONS].delete()

    branding_image = BrandingImage.objects.all()

    return {"branding_image": branding_image}


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()

    return {"notifications": allnotifications}
