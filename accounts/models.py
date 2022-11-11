from web.functions import generate_pk
from web.functions import generate_pw

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField


class User(AbstractUser):
    CATEGORY_CHOICES = (
        ("AKSHAYA", "AKSHAYA"),
        ("CSC(DIGITAL INDIA)", "CSC(DIGITAL INDIA)"),
        ("ONLINE SERVICE CENTER", "ONLINE SERVICE CENTER"),
        ("DTP AND PHOTOSTAT SHOP", "DTP AND PHOTOSTAT SHOP"),
        ("MOBILE SHOP", "MOBILE SHOP"),
        ("TRAVELS", "TRAVELS"),
        ("BANKING KIOSK", "BANKING KIOSK"),
        ("INTERNET CAFE", "INTERNET CAFE"),
        ("OTHERS", "OTHERS"),
    )
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,15}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True, blank=True)
    phone = models.CharField(_("phone number"), validators=[phone_regex], max_length=17, unique=True)
    temp_password = models.CharField("Temporary password", default=generate_pw, max_length=17)
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=100)
    profile_image = VersatileImageField(upload_to="Profile", null=True, blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    def __str__(self):
        return str(self.id)
