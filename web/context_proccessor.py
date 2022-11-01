from notification.models import BroadcastNotification
from services.models import BrandingImage


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()

    return {"notifications": allnotifications}


def main_context(request):
    branding_image = BrandingImage.objects.all()

    return {"branding_image": branding_image}
