from .models import Order
from django.shortcuts import redirect


def subscription_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            subs = Order.objects.filter(user=request.user, is_active=True).last()
            if request.user.is_superuser:
                return func(request, *args, **kwargs)
            elif subs.is_valid:
                return func(request, *args, **kwargs)
            else:
                return redirect("web:expired")
        else:
            return redirect("web:login_view")

    return wrapper
