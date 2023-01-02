# Generated by Django 4.1.1 on 2022-12-31 12:33

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL), ("services", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100, unique=True)),
                ("phone_no", models.CharField(max_length=15, unique=True)),
                ("address", models.CharField(max_length=100)),
                ("created_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "Customer", "verbose_name_plural": "Customers"},
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("invoice_name", models.CharField(max_length=100)),
                ("invoice_no", models.CharField(max_length=100)),
                ("created", models.DateField(auto_now_add=True)),
                ("customer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="invoices.customer")),
            ],
            options={"verbose_name": "Invoice", "verbose_name_plural": "Invoices"},
        ),
        migrations.CreateModel(
            name="InvoiceItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("services_charge", models.CharField(max_length=100)),
                ("sub_total", models.PositiveIntegerField(blank=True, editable=False, verbose_name="Sub Total")),
                ("username", models.CharField(blank=True, max_length=100, null=True)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("descripton", models.TextField(blank=True, null=True)),
                ("qty", models.PositiveIntegerField(verbose_name="Quantity")),
                ("created", models.DateField(auto_now_add=True)),
                ("invoice", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="invoices.invoice")),
                ("services_name", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="invoices_items", to="services.services")),
            ],
            options={"verbose_name": "Invoice Item", "verbose_name_plural": "Invoice Items"},
        ),
    ]
