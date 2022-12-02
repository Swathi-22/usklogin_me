# Generated by Django 4.1.1 on 2022-12-02 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import versatileimagefield.fields
import web.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="AddonServices",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Agent_Bonus/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Add-on Services"},
        ),
        migrations.CreateModel(
            name="AgencyPortal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Agency_Portal/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Agency Portals"},
        ),
        migrations.CreateModel(
            name="AgentBonus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Agent_Bonus/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Bonus for USK Agent"},
        ),
        migrations.CreateModel(
            name="BackOfficeServices",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Back_Office_Service/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Back Office Service"},
        ),
        migrations.CreateModel(
            name="CallSupport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=50)),
            ],
            options={"verbose_name_plural": "Call Support"},
        ),
        migrations.CreateModel(
            name="CommonServicesPoster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="CommonServices/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Common Services Poster"},
        ),
        migrations.CreateModel(
            name="DownloadDocuments",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.FileField(upload_to="")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Documents/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Download Documents"},
        ),
        migrations.CreateModel(
            name="DownloadForms",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.FileField(upload_to="")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Forms/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Download Forms"},
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("question", models.CharField(max_length=500)),
                ("answer", models.TextField()),
            ],
            options={"verbose_name_plural": "FAQ"},
        ),
        migrations.CreateModel(
            name="FestivelPoster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="FestivelPoster/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Festivel Poster"},
        ),
        migrations.CreateModel(
            name="ImportantPoster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Importants/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Important Poster"},
        ),
        migrations.CreateModel(
            name="LatestNews",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("news", models.TextField()),
                ("link", models.URLField(blank=True, null=True)),
            ],
            options={"verbose_name_plural": "Lates News"},
        ),
        migrations.CreateModel(
            name="MarketingTips",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Marketing_Tip/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Marketing Tips"},
        ),
        migrations.CreateModel(
            name="NewServicePoster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="New_Service/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Newly Added Service Poster"},
        ),
        migrations.CreateModel(
            name="OtherIdeas",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Other_Ideas/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Other Ideas"},
        ),
        migrations.CreateModel(
            name="ProfessionalPoster",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=150)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="ProfessionalPoster/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Professional Poster"},
        ),
        migrations.CreateModel(
            name="Softwares",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Softwares/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Softwares"},
        ),
        migrations.CreateModel(
            name="SupportRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
            options={"verbose_name_plural": "Support Request"},
        ),
        migrations.CreateModel(
            name="SupportTicket",
            fields=[
                ("ticket_id", models.CharField(blank=True, default=web.functions.generate_ticket_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
            options={"verbose_name_plural": "Support Ticket"},
        ),
        migrations.CreateModel(
            name="Tools",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("image", versatileimagefield.fields.VersatileImageField(upload_to="Tools/", verbose_name="Image")),
                ("ppoi", versatileimagefield.fields.PPOIField(default="0.5x0.5", editable=False, max_length=20, verbose_name="Image PPOI")),
                ("link", models.URLField()),
                ("detail_link", models.URLField()),
            ],
            options={"verbose_name_plural": "Tools"},
        ),
        migrations.CreateModel(
            name="WhatsappSupport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=50)),
            ],
            options={"verbose_name_plural": "Whatsapp Support"},
        ),
        migrations.CreateModel(
            name="Subscription",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.FloatField(verbose_name="Amount")),
                ("is_active", models.BooleanField(default=False, verbose_name="Mark as Active")),
                ("valid_from", models.DateTimeField(default=django.utils.timezone.now)),
                ("valid_upto", models.DateTimeField(blank=True, editable=False)),
                ("status", models.CharField(default="Pending", max_length=254, verbose_name="Payment Status")),
                ("provider_order_id", models.CharField(blank=True, max_length=40, null=True, verbose_name="Order ID")),
                ("payment_id", models.CharField(blank=True, max_length=36, null=True, verbose_name="Payment ID")),
                ("signature_id", models.CharField(blank=True, max_length=128, null=True, verbose_name="Signature ID")),
                ("is_notified", models.BooleanField(default=False, verbose_name="Is Notified")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="upgraded_user", to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "User Subscription", "verbose_name_plural": "User Subscriptions"},
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.FloatField(verbose_name="Amount")),
                ("status", models.CharField(default="Pending", max_length=254, verbose_name="Payment Status")),
                ("provider_order_id", models.CharField(blank=True, max_length=40, null=True, verbose_name="Order ID")),
                ("payment_id", models.CharField(blank=True, max_length=36, null=True, verbose_name="Payment ID")),
                ("signature_id", models.CharField(blank=True, max_length=128, null=True, verbose_name="Signature ID")),
                ("valid_from", models.DateTimeField(default=django.utils.timezone.now)),
                ("valid_upto", models.DateTimeField(blank=True, editable=False)),
                ("is_active", models.BooleanField(default=False, verbose_name="Mark as Active")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
