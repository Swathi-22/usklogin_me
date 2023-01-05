from datetime import timedelta

from accounts.models import User

from .constants import PaymentStatus
from .functions import generate_ticket_pk
from django.db import models
from django.utils import timezone
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


PAYMENT_STATUS_CHOICES = (("Success", "Success"), ("Failure", "Failure"), ("Pending", "Pending"))
TYPE_CHOICES = (("Access", "Access"),)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(("Amount"), null=False, blank=False)
    status = models.CharField(("Payment Status"), default=PaymentStatus.PENDING, max_length=254, choices=PAYMENT_STATUS_CHOICES)
    types = models.CharField(("Type"), max_length=254, choices=TYPE_CHOICES)
    provider_order_id = models.CharField(("Order ID"), max_length=40, null=True, blank=True)
    payment_id = models.CharField(("Payment ID"), max_length=36, null=True, blank=True)
    signature_id = models.CharField(("Signature ID"), max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.user}-{self.status}"


class LatestNews(models.Model):
    news = models.TextField()
    link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Lates News"

    def __str__(self):
        return str(self.news)


class NewServicePoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="New_Service/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Newly Added Service Poster"

    def __str__(self):
        return str(self.image)


class ImportantPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Importants/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Important Poster"

    def __str__(self):
        return str(self.image)


class CommonServicesPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="CommonServices/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Common Services Poster"

    def __str__(self):
        return str(self.image)


class FestivelPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="FestivelPoster/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Festivel Poster"

    def __str__(self):
        return str(self.image)


class ProfessionalPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="ProfessionalPoster/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Professional Poster"

    def __str__(self):
        return str(self.image)


class AgencyPortalService(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Agency_Portal_Services/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Agency Portal Services"

    def __str__(self):
        return str(self.image)


class SeasonalService(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Seasonal_Services/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Seasonal Services"

    def __str__(self):
        return str(self.image)


class UpdatesorInformation(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Updates_or_Information/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Updates/Information"

    def __str__(self):
        return str(self.image)


class PromotionalPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Promotional_Poster/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Promotional Poster"

    def __str__(self):
        return str(self.image)


class Others(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Others/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Others"

    def __str__(self):
        return str(self.image)


class DownloadForms(models.Model):
    CATEGORY_CHOICES = (
        ("Village Services Related", "Village Services Related"),
        ("Panchayath Related", "Panchayath Related"),
        ("Students Related", "Students Related"),
        ("Pension Scheme Related", "Pension Scheme Related"),
        ("Income Tax Department", "Income Tax Department"),
        ("Others", "Others"),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, blank=True, null=True)
    file = models.FileField()
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Forms/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Download Forms"

    def __str__(self):
        return str(self.name)


class DownloadDocuments(models.Model):
    CATEGORY_CHOICES = (("CV Formats", "CV Formats"), ("Agreement Models", "Agreement Models"), ("Business Related", "Business Related"), ("Others", "Others"))
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    file = models.FileField()
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Documents/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Download Documents"

    def __str__(self):
        return str(self.name)


class Softwares(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Softwares/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Softwares"

    def __str__(self):
        return str(self.name)


class Tools(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Tools/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Tools"

    def __str__(self):
        return str(self.name)


class MarketingTips(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Marketing_Tip/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Marketing Tips"

    def __str__(self):
        return str(self.name)


class OtherIdeas(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Other_Ideas/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Add to the Business"

    def __str__(self):
        return str(self.name)


class AgencyPortal(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Agency_Portal/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Agency Portals"

    def __str__(self):
        return str(self.name)


class BackOfficeServices(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Back_Office_Service/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Back Office Service"

    def __str__(self):
        return str(self.name)


class AgentBonus(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Agent_Bonus/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Bonus for USK Agent"

    def __str__(self):
        return str(self.name)


class SupportRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Support Request"

    def __str__(self):
        return str(self.name)


class SupportTicket(models.Model):
    ticket_id = models.CharField(default=generate_ticket_pk, primary_key=True, max_length=255, unique=True, blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Support Ticket"

    def __str__(self):
        return str(self.name)


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    class Meta:
        verbose_name_plural = "FAQ"

    def __str__(self):
        return str(self.question)


class CallSupport(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Call Support"

    def __str__(self):
        return str(self.name)


class WhatsappSupport(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Whatsapp Support"

    def __str__(self):
        return str(self.name)


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name="upgraded_user", on_delete=models.CASCADE)
    amount = models.FloatField("Amount", null=False, blank=False)
    valid_from = models.DateTimeField(default=timezone.now)
    valid_upto = models.DateTimeField(blank=True, editable=True)
    status = models.CharField("Payment Status", default=PaymentStatus.PENDING, max_length=254, choices=PAYMENT_STATUS_CHOICES)
    types = models.CharField(("Subscription Type"), max_length=254, choices=TYPE_CHOICES, default="Access")
    provider_order_id = models.CharField("Order ID", max_length=40, null=True, blank=True)
    payment_id = models.CharField("Payment ID", max_length=36, null=True, blank=True)
    signature_id = models.CharField("Signature ID", max_length=128, null=True, blank=True)
    is_notified = models.BooleanField("Is Notified", default=False)

    class Meta:
        verbose_name = "User Subscription"
        verbose_name_plural = "User Subscriptions"

    @property
    def is_valid(self):
        if self.types == "Access":
            return True if self.valid_from + timedelta(days=365) >= timezone.now() else False
        elif self.types == "Support":
            return True if self.valid_from + timedelta(days=30) >= timezone.now() else False

    @property
    def is_active(self):
        if self.types == "Access":
            return True if self.valid_from + timedelta(days=365) >= timezone.now() else False
        elif self.types == "Support":
            return True if self.valid_from + timedelta(days=30) >= timezone.now() else False

    def __str__(self):
        return str(f"{self.user} - {self.valid_from} - {self.valid_upto}")

    def save(self, *args, **kwargs):
        if self.types == "Access":
            self.valid_upto = self.valid_from + timedelta(days=365)
        elif self.types == "Support":
            self.valid_upto = self.valid_from + timedelta(days=30)
        super().save(*args, **kwargs)


class AddonServices(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Agent_Bonus/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()
    detail_link = models.URLField()

    class Meta:
        verbose_name_plural = "Add-on Services"

    def __str__(self):
        return str(self.name)


class OnloadPopup(models.Model):
    title = models.TextField()
    image = VersatileImageField("Image", upload_to="Onload_Popup/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Onload Popup"

    def __str__(self):
        return str(self.title)
