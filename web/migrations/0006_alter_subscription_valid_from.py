# Generated by Django 4.1.1 on 2022-11-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("web", "0005_remove_subscription_days")]

    operations = [migrations.AlterField(model_name="subscription", name="valid_from", field=models.DateTimeField(auto_now_add=True))]
