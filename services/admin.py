from .models import BrandingImage
from .models import ServiceHeads
from .models import Services
from django.contrib import admin


@admin.register(ServiceHeads)
class ServiceHeadsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("service_head", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BrandingImage)
class BrandingImageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "image", "is_verified")
