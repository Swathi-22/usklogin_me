# Generated by Django 4.1.1 on 2022-11-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("web", "0001_initial")]

    operations = [
        migrations.AddField(model_name="subscription", name="payment_id", field=models.CharField(blank=True, max_length=36, null=True, verbose_name="Payment ID")),
        migrations.AddField(model_name="subscription", name="provider_order_id", field=models.CharField(blank=True, max_length=40, null=True, verbose_name="Order ID")),
        migrations.AddField(model_name="subscription", name="signature_id", field=models.CharField(blank=True, max_length=128, null=True, verbose_name="Signature ID")),
        migrations.AddField(model_name="subscription", name="status", field=models.CharField(default="Pending", max_length=254, verbose_name="Payment Status")),
    ]