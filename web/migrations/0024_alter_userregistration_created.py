# Generated by Django 4.1.1 on 2022-11-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_alter_userregistration_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
