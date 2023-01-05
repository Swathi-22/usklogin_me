from .models import Subscription
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone


def subscription_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if Subscription.objects.filter(user=request.user, status="Success", types="Access", valid_upto__gt=timezone.now()).exists():
                return func(request, *args, **kwargs)
            else:
                return redirect("web:order_payment")
        else:
            return HttpResponseRedirect("/start/")
    return wrapper
