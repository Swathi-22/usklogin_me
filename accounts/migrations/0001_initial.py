# Generated by Django 4.1.1 on 2022-11-17 11:11

import web.functions

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.utils.timezone
import versatileimagefield.fields
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0012_alter_user_first_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False, help_text="Designates that this user has all permissions without explicitly assigning them.", verbose_name="superuser status"
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("is_staff", models.BooleanField(default=False, help_text="Designates whether the user can log into this admin site.", verbose_name="staff status")),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.", verbose_name="active"
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("id", models.CharField(blank=True, default=web.functions.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                (
                    "phone",
                    models.CharField(
                        max_length=17,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex="^\\+?1?\\d{9,15}$"
                            )
                        ],
                        verbose_name="phone number",
                    ),
                ),
                ("temp_password", models.CharField(blank=True, max_length=17, verbose_name="Temporary password")),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("shop_name", models.CharField(max_length=100)),
                ("shop_address", models.TextField()),
                ("district", models.CharField(max_length=200)),
                ("pincode", models.CharField(max_length=100)),
                ("profile_image", versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to="Profile")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("AKSHAYA", "AKSHAYA"),
                            ("CSC(DIGITAL INDIA)", "CSC(DIGITAL INDIA)"),
                            ("ONLINE SERVICE CENTER", "ONLINE SERVICE CENTER"),
                            ("DTP AND PHOTOSTAT SHOP", "DTP AND PHOTOSTAT SHOP"),
                            ("MOBILE SHOP", "MOBILE SHOP"),
                            ("TRAVELS", "TRAVELS"),
                            ("BANKING KIOSK", "BANKING KIOSK"),
                            ("INTERNET CAFE", "INTERNET CAFE"),
                            ("OTHERS", "OTHERS"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "user", "verbose_name_plural": "users", "abstract": False},
            managers=[("objects", django.contrib.auth.models.UserManager())],
        )
    ]
