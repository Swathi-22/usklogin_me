from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from web.forms import UserRegistrationForm

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("web:login_view")
    template_name = "web/register.html"
