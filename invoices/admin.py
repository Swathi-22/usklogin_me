from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from .resources import InvoiceAdminResource
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("invoice", "services_name", "created", "sub_total")


@admin.register(Invoice)
class InvoiceExcelAdmin(ImportExportModelAdmin):
    list_display = ("customer", "invoice_name", "invoice_no")
    resource_class = InvoiceAdminResource
