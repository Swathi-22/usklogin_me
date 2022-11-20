# Generated by Django 4.1.1 on 2022-11-15 08:35

import user_sessions.models

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                ("session_key", models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name="session key")),
                ("session_data", models.TextField(verbose_name="session data")),
                ("expire_date", models.DateTimeField(db_index=True, verbose_name="expiry date")),
                ("user_agent", models.CharField(blank=True, max_length=200, null=True)),
                ("last_activity", models.DateTimeField(auto_now=True)),
                ("ip", models.GenericIPAddressField(blank=True, null=True, verbose_name="IP")),
                ("user", models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "session", "verbose_name_plural": "sessions"},
            managers=[("objects", user_sessions.models.SessionManager())],
        )
    ]
