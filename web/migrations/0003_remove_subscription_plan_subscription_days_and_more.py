# Generated by Django 4.1.1 on 2022-11-18 10:05

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("web", "0002_plan_subscription")]

    operations = [
        migrations.RemoveField(model_name="subscription", name="plan"),
        migrations.AddField(model_name="subscription", name="days", field=models.PositiveIntegerField(blank=True, default=30)),
        migrations.AddField(model_name="subscription", name="is_active", field=models.BooleanField(default=False, verbose_name="Mark as Active")),
        migrations.AlterField(model_name="subscription", name="valid_from", field=models.DateTimeField(auto_now_add=True, db_index=True)),
        migrations.DeleteModel(name="Plan"),
    ]
