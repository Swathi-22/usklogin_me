from accounts.models import User
from services.models import BrandingImage

from .models import support_request
from .models import support_ticket
from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "phone", "category", "email", "shop_name", "shop_address", "district", "pincode")
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "required": "required"}),
            "phone": TextInput(attrs={"class": "form-control", "required": "required", "type": "tel"}),
            "category": Select(attrs={"class": "form-control", "required": "required"}),
            "email": EmailInput(attrs={"class": "form-control", "required": "required"}),
            "shop_name": TextInput(attrs={"class": "form-control", "required": "required"}),
            "shop_address": TextInput(attrs={"class": "form-control", "required": "required"}),
            "district": TextInput(attrs={"class": "form-control", "required": "required"}),
            "pincode": TextInput(attrs={"class": "form-control", "required": "required"}),
        }


class support_requestForm(forms.ModelForm):
    class Meta:
        model = support_request
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={"class": "form-control", "name": "name", "id": "name", "required": "required", "autocomplete": "off"}),
            "phone": TextInput(attrs={"class": "form-control", "name": "phoneno", "id": "phoneno", "required": "required", "autocomplete": "off"}),
            "email": EmailInput(attrs={"class": "form-control", "name": "email", "id": "email", "required": "required", "autocomplete": "off"}),
            "message": Textarea(attrs={"class": "form-control", "name": "message", "id": "message", "rows": "6", "autocomplete": "off"}),
        }


class support_ticketForm(forms.ModelForm):
    class Meta:
        model = support_ticket
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
        fields = ("profile_image",)
        widgets = {"profile_image": FileInput(attrs={"class": "form-control", "name": "image"})}


class BrandingImageForm(forms.ModelForm):
    class Meta:
        model = BrandingImage
        fields = ("image",)
        widgets = {"image": FileInput(attrs={"class": "get-input"})}
