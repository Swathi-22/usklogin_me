from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import EmailInput
from django.forms.widgets import FileInput
from django.forms.widgets import Select
from django.forms.widgets import Textarea
from django.forms.widgets import TextInput

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "name",
            "shop_name",
            "shop_address",
            "email",
            "phone",
            "district",
            "pincode",
            "category",
        )
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "name",
                    "id": "name",
                    "required": "required",
                }
            ),
            "shop_name": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "shop_name",
                    "id": "shop_name",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "shop_address": Textarea(
                attrs={
                    "class": "input-field",
                    "name": "shop_address",
                    "id": "shop_address",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "input-field",
                    "name": "email",
                    "id": "email",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "phone",
                    "id": "phone",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "district": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "district",
                    "id": "district",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "pincode": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "pincode",
                    "id": "pincode",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "category": Select(
                attrs={
                    "class": "input-field",
                    "name": "category",
                    "id": "category",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "name",
            "shop_name",
            "shop_address",
            "email",
            "phone",
            "district",
            "pincode",
            "category",
        )

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "name",
                    "id": "name",
                    "required": "required",
                }
            ),
            "shop_name": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "shop_name",
                    "id": "shop_name",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "shop_address": Textarea(
                attrs={
                    "class": "input-field",
                    "name": "shop_address",
                    "id": "shop_address",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "input-field",
                    "name": "email",
                    "id": "email",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "phone",
                    "id": "phone",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "district": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "district",
                    "id": "district",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "pincode": TextInput(
                attrs={
                    "class": "input-field",
                    "name": "pincode",
                    "id": "pincode",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
            "category": Select(
                attrs={
                    "class": "input-field",
                    "name": "category",
                    "id": "category",
                    "required": "required",
                    "autocomplete": "off",
                }
            ),
        }
