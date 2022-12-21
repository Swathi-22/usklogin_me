from accounts.models import User
from services.models import BrandingImage

from .models import SupportRequest
from .models import SupportTicket
from django import forms
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput


class SupportRequestForm(forms.ModelForm):
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
        fields = ("profile_image",)
        widgets = {"profile_image": FileInput(attrs={"class": "form-control", "name": "image"})}


class BrandingImageForm(forms.ModelForm):
    class Meta:
        model = BrandingImage
        fields = ("image",)
        widgets = {"image": FileInput(attrs={"class": "get-input"})}
