from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def subscription_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_subscribed:
                return func(request, *args, **kwargs)
            else:
                return redirect("web:expired")
        else:
            return redirect("web:login_view")
    return wrapper