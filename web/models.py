from accounts.models import User

from .constants import PaymentStatus
from .functions import generate_ticket_pk
from django.db import models
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(("Amount"), null=False, blank=False)
    status = models.CharField(("Payment Status"), default=PaymentStatus.PENDING, max_length=254)
    provider_order_id = models.CharField(("Order ID"), max_length=40, null=True, blank=True)
    payment_id = models.CharField(("Payment ID"), max_length=36, null=True, blank=True)
    signature_id = models.CharField(("Signature ID"), max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


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

    class Meta:
        verbose_name_plural = "New Service Poster"

    def __str__(self):
        return str(self.image)


class ImportantPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="Importants/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Important Poster"

    def __str__(self):
        return str(self.image)


class CommonServicesPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="CommonServices/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Common Services Poster"

    def __str__(self):
        return str(self.image)


class FestivelPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="FestivelPoster/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Festivel Poster"

    def __str__(self):
        return str(self.image)


class ProfessionalPoster(models.Model):
    title = models.CharField(max_length=150)
    image = VersatileImageField("Image", upload_to="ProfessionalPoster/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Professional Poster"

    def __str__(self):
        return str(self.image)


class DownloadForms(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Forms/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Download Forms"

    def __str__(self):
        return str(self.name)


class DownloadDocuments(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Documents/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Download Documents"

    def __str__(self):
        return str(self.name)


class Softwares(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Softwares/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Softwares"

    def __str__(self):
        return str(self.name)


class Tools(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Tools/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Tools"

    def __str__(self):
        return str(self.name)


class MarketingTips(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Marketing_Tip/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Marketing Tips"

    def __str__(self):
        return str(self.name)


class OtherIdeas(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Other_Ideas/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Other Ideas"

    def __str__(self):
        return str(self.name)


class AgencyPortal(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Agency_Portal/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Agency Portals"

    def __str__(self):
        return str(self.name)


class BackOfficeServices(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Back_Office_Service/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

    class Meta:
        verbose_name_plural = "Back Office Service"

    def __str__(self):
        return str(self.name)


class AgentBonus(models.Model):
    name = models.CharField(max_length=100)
    image = VersatileImageField("Image", upload_to="Agent_Bonus/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link = models.URLField()

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


class ChangePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class CertificateImages(models.Model):
    usk_logo = VersatileImageField(upload_to="USKimages", null=True, default="USK Login Logo.png")
    bruvsha_logo = VersatileImageField(upload_to="USKimages", null=True, default="Bruvsha Logo.png")
    seal = VersatileImageField(upload_to="USKimages", null=True, default="Seal.png")
    sign = VersatileImageField(upload_to="USKimages", null=True, default="Sign.png")


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
