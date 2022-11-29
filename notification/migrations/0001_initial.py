# Generated by Django 4.1.1 on 2022-11-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BroadcastNotification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("message", models.TextField()),
                ("broadcast_on", models.DateTimeField()),
                ("sent", models.BooleanField(default=False)),
            ],
            options={"ordering": ["-broadcast_on"]},
        )
    ]
