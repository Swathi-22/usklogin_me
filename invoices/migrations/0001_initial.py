# Generated by Django 4.1.1 on 2022-11-09 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [("services", "0001_initial")]

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
            ],
            options={"verbose_name": "Customer", "verbose_name_plural": "Customers"},
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("invoice_name", models.CharField(max_length=100)),
                ("invoice_no", models.CharField(max_length=100)),
                ("from_address", models.CharField(max_length=100)),
                ("created", models.DateField(auto_now_add=True)),
                ("phone_no", models.CharField(max_length=15, unique=True)),
                ("customer", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="invoices.customer")),
            ],
            options={"verbose_name": "Invoice", "verbose_name_plural": "Invoices"},
        ),
        migrations.CreateModel(
            name="InvoiceItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("services_charge", models.IntegerField()),
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
