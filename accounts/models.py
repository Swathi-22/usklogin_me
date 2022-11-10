from web.functions import generate_pk
from web.functions import generate_pw

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from versatileimagefield.fields import VersatileImageField


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError("The given phone must be set")
        self.phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    """User model."""

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

    username = None
    email = models.EmailField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,15}$", message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(_("phone number"), validators=[phone_regex], max_length=17, unique=True)  # validators should be a list
    password = models.CharField(_("password"), default=generate_pw, max_length=17, unique=True)  # validators should be a list
    id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    shop_address = models.TextField()
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=100)
    profile_image = VersatileImageField(upload_to="Profile", null=True, blank=True)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    is_user = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.id
