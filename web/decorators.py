from django.core.exceptions import PermissionDenied
from functools import wraps

from .models import Subscription

def requires_subscription(view):
    @wraps(view)
    def _view(request, *args, **kwargs):
        user=request.user
        if not Subscription.objects.filter(user=user, is_active=True).exists():
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return _view
