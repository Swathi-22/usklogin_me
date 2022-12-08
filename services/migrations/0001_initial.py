# Generated by Django 4.1.1 on 2022-12-08 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="ServiceHeads",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=225)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={"verbose_name_plural": "Service Head"},
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=225)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="service/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link_to_official_website", models.URLField()),
                ("about_service", tinymce.models.HTMLField(blank=True, null=True)),
                ("requirements", tinymce.models.HTMLField(blank=True, null=True)),
                ("service_charge", models.CharField(max_length=100)),
                ("actual_service_charge", models.CharField(max_length=100)),
                ("video_tutorial", models.CharField(max_length=100)),
                ("guidline", models.CharField(max_length=100)),
                ("upload_form", models.URLField()),
                ("slug", models.SlugField(unique=True)),
                ("service_head", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="services.serviceheads")),
            ],
            options={"verbose_name_plural": "Services"},
        ),
        migrations.CreateModel(
            name="BrandingImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="service/", verbose_name="Image")),
                ("is_verified", models.BooleanField(default=False, verbose_name="Mark as Verified")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "Branding Image"},
        ),
    ]
