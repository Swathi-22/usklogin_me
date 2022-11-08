from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from django.contrib import admin
# from import_export.admin import ExportMixinAdmin
from import_export import resources
from import_export.fields import Field

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


class BookResource(resources.ModelResource):
    customer = Field()
    class Meta:
        model = Invoice


# class InvoiceAdmin(ExportMixinAdmin):
#     resource_class = BookResource


# admin.site.register(InvoiceAdmin)