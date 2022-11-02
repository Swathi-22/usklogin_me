from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from django.contrib import admin


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("customer", "invoice_name", "invoice_no")


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("invoice", "services_name", "created")
