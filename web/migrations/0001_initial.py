# Generated by Django 4.1.1 on 2022-11-10 11:37

from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields
import web.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyPortal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Agency_Portal/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Agency Portals',
            },
        ),
        migrations.CreateModel(
            name='AgentBonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Agent_Bonus/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Bonus for USK Agent',
            },
        ),
        migrations.CreateModel(
            name='BackOfficeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Back_Office_Service/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Back Office Service',
            },
        ),
        migrations.CreateModel(
            name='CallSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Call Support',
            },
        ),
        migrations.CreateModel(
            name='CertificateImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usk_logo', versatileimagefield.fields.VersatileImageField(default='USK Login Logo.png', null=True, upload_to='USKimages')),
                ('bruvsha_logo', versatileimagefield.fields.VersatileImageField(default='Bruvsha Logo.png', null=True, upload_to='USKimages')),
                ('seal', versatileimagefield.fields.VersatileImageField(default='Seal.png', null=True, upload_to='USKimages')),
                ('sign', versatileimagefield.fields.VersatileImageField(default='Sign.png', null=True, upload_to='USKimages')),
            ],
        ),
        migrations.CreateModel(
            name='CommonServicesPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='CommonServices/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Common Services Poster',
            },
        ),
        migrations.CreateModel(
            name='DownloadDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Documents/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Download Documents',
            },
        ),
        migrations.CreateModel(
            name='DownloadForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Forms/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Download Forms',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='FestivelPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='FestivelPoster/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Festivel Poster',
            },
        ),
        migrations.CreateModel(
            name='ImportantPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Importants/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Important Poster',
            },
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Lates News',
            },
        ),
        migrations.CreateModel(
            name='MarketingTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Marketing_Tip/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Marketing Tips',
            },
        ),
        migrations.CreateModel(
            name='NewServicePoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='New_Service/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'New Service Poster',
            },
        ),
        migrations.CreateModel(
            name='OtherIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Other_Ideas/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Other Ideas',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='ProfessionalPoster/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Professional Poster',
            },
        ),
        migrations.CreateModel(
            name='Softwares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Softwares/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Softwares',
            },
        ),
        migrations.CreateModel(
            name='SupportRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Support Request',
            },
        ),
        migrations.CreateModel(
            name='SupportTicket',
            fields=[
                ('ticket_id', models.CharField(blank=True, default=web.functions.generate_ticket_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Support Ticket',
            },
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Tools/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.CharField(blank=True, default=web.functions.generate_pk, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, default=web.functions.generate_pw, max_length=30)),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=100)),
                ('profile_image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='Profile')),
                ('category', models.CharField(choices=[('AKSHAYA', 'AKSHAYA'), ('CSC(DIGITAL INDIA)', 'CSC(DIGITAL INDIA)'), ('ONLINE SERVICE CENTER', 'ONLINE SERVICE CENTER'), ('DTP AND PHOTOSTAT SHOP', 'DTP AND PHOTOSTAT SHOP'), ('MOBILE SHOP', 'MOBILE SHOP'), ('TRAVELS', 'TRAVELS'), ('BANKING KIOSK', 'BANKING KIOSK'), ('INTERNET CAFE', 'INTERNET CAFE'), ('OTHERS', 'OTHERS')], max_length=200)),
                ('is_user', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Resgistered Users',
            },
        ),
        migrations.CreateModel(
            name='WhatsappSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Whatsapp Support',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(default='Pending', max_length=254, verbose_name='Payment Status')),
                ('provider_order_id', models.CharField(max_length=40, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, verbose_name='Signature ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forgot_password_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.userregistration')),
            ],
        ),
    ]
