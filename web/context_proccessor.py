from accounts.models import User
from django.conf import settings

from notification.models import BroadcastNotification
from services.models import BrandingImage





def main_context(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    if request.user.is_authenticated:
        if user.session_set.all().count() > settings.MAX_DEVICE_SESSIONS:
            user.session_set.all().order_by('-last_activity')[:3].delete()

    branding_image = BrandingImage.objects.all()

    return {"branding_image": branding_image}


    def notifications(request):
        allnotifications = BroadcastNotification.objects.all()

        return {"notifications": allnotifications}
