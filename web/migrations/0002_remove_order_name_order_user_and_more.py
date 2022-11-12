# Generated by Django 4.1.1 on 2022-11-12 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='changepassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='Payment ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='provider_order_id',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Order ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='signature_id',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Signature ID'),
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
    ]