from .models import Note
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.forms import widgets


class UserRegistrationForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,15}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    class Meta:
        model = User
        fields = ("name", "phone", "category", "email", "shop_name", "shop_address", "district", "pincode","referal_code", "password1", "password2")
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "phone": widgets.TextInput(attrs={"class": "form-control", "required": "required", "type": "tel"}),
            "category": widgets.Select(attrs={"class": "form-control", "required": "required"}),
            "email": widgets.EmailInput(attrs={"class": "form-control", "required": "required"}),
            "shop_name": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "shop_address": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "district": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "pincode": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "referal_code":widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("title", "note")
        widgets = {
            "title": widgets.TextInput(attrs={"class": "form-control", "required": "required"}),
            "note": widgets.Textarea(attrs={"class": "form-control", "required": "required"}),
        }
