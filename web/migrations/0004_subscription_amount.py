# Generated by Django 4.1.1 on 2022-11-18 10:13

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("web", "0003_remove_subscription_plan_subscription_days_and_more")]

    operations = [migrations.AddField(model_name="subscription", name="amount", field=models.FloatField(default=400, verbose_name="Amount"), preserve_default=False)]
