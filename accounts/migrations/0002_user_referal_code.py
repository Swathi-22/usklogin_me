# Generated by Django 4.1.1 on 2023-01-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [migrations.AddField(model_name="user", name="referal_code", field=models.CharField(blank=True, max_length=20, null=True))]