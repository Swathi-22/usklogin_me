from accounts.models import User

from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import PPOIField
from versatileimagefield.fields import VersatileImageField


# Service category
class ServiceHeads(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Service Head"

    def __str__(self):
        return str(self.title)


# Services in service category
class Services(models.Model):
    service_head = models.ForeignKey(ServiceHeads, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    image = VersatileImageField("Image", upload_to="service/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    link_to_official_website = models.URLField()
    about_service = HTMLField(blank=True, null=True)
    requirements = HTMLField(blank=True, null=True)
    service_charge = models.CharField(max_length=100)
    actual_service_charge = models.CharField(max_length=100)
    video_tutorial = models.CharField(max_length=100)
    guidline = models.CharField(max_length=100)
    upload_form = models.URLField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return str(self.title)


class BrandingImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = VersatileImageField("Image", upload_to="service/", blank=True, null=True)
    is_verified = models.BooleanField("Mark as Verified", default=False)

    class Meta:
        verbose_name = "Branding Image"

    def __str__(self):
        return str(self.image)
