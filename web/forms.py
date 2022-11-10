import re

from attr import fields
import attr

from accounts.models import User
from .models import SupportRequest, SupportTicket
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from web.functions import generate_pw

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistration
#         fields = '__all__'
#         widgets= {
#             'name': TextInput(attrs={'class':'login__input','name':'name','id':'name','required':'required',}),
#             'password':TextInput(attrs={'class':'login__input','type':'password','name':'password','id':'password','required':'required',})
#         }


def phone_number_validation(value):
    if not re.compile(r"[0-9]\d{9}$").match(value):
        raise ValidationError("This is Not Valid Phone Number")


class UserRegistrationForm(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validation])

    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "input-field", "name": "name", "id": "name", "required": "required"}),
            "shop_name": TextInput(attrs={"class": "input-field", "name": "shop_name", "id": "shop_name", "required": "required", "autocomplete": "off"}),
            "shop_address": Textarea(attrs={"class": "input-field", "name": "shop_address", "id": "shop_address", "required": "required", "autocomplete": "off"}),
            "email": EmailInput(attrs={"class": "input-field", "name": "email", "id": "email", "required": "required", "autocomplete": "off"}),
            "phone": TextInput(attrs={"class": "input-field", "name": "phone", "id": "phone", "required": "required", "autocomplete": "off"}),
            "district": TextInput(attrs={"class": "input-field", "name": "district", "id": "district", "required": "required", "autocomplete": "off"}),
            "pincode": TextInput(attrs={"class": "input-field", "name": "pincode", "id": "pincode", "required": "required", "autocomplete": "off"}),
            "category": Select(attrs={"class": "input-field", "name": "category", "id": "category", "required": "required", "autocomplete": "off"}),
        }


class SupportRequestForm(forms.ModelForm):
    # phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = SupportRequest
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "name": "name", "id": "name", "required": "required", "autocomplete": "off"}),
            "phone": TextInput(attrs={"class": "form-control", "name": "phoneno", "id": "phoneno", "required": "required", "autocomplete": "off"}),
            "email": EmailInput(attrs={"class": "form-control", "name": "email", "id": "email", "required": "required", "autocomplete": "off"}),
            "message": Textarea(attrs={"class": "form-control", "name": "message", "id": "message", "rows": "6", "autocomplete": "off"}),
        }


class SupportTicketForm(forms.ModelForm):
    # phone = forms.CharField(validators=[phone_number_validation])
    class Meta:
        model = SupportTicket
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "name": "name", "id": "name", "required": "required", "autocomplete": "off"}),
            "phone": TextInput(attrs={"class": "form-control", "name": "phoneno", "id": "phoneno", "required": "required", "autocomplete": "off"}),
            "email": EmailInput(attrs={"class": "form-control", "name": "email", "id": "email", "required": "required", "autocomplete": "off"}),
            "message": Textarea(attrs={"class": "form-control", "name": "message", "id": "message", "rows": "6", "autocomplete": "off"}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "name": "name"}),
            "password": TextInput(attrs={"class": "form-control", "name": "password", "required": "required", "autocomplete": "off"}),
            "shop_name": TextInput(attrs={"class": "form-control", "name": "shop_name"}),
            "shop_address": Textarea(attrs={"class": "form-control", "name": "shop_address"}),
            "email": EmailInput(attrs={"class": "form-control", "name": "email"}),
            "phone": TextInput(attrs={"class": "form-control", "name": "phone", "required": "required", "autocomplete": "off"}),
            "district": TextInput(attrs={"class": "form-control", "name": "district"}),
            "pincode": TextInput(attrs={"class": "form-control", "name": "pincode"}),
            "category": Select(attrs={"class": "form-control", "name": "category"}),
            "profile_image": FileInput(attrs={"class": "form-control", "name": "image"}),
        }
