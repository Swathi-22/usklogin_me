from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import InvoiceAdminResource
# from import_export.fields import Field
# from import_export import resources
# from import_export.admin import ExportMixin
# from import_export.formats import base_formats
# from import_export.widgets import ForeignKeyWidget

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


# @admin.register(Invoice)
# class InvoiceAdmin(ImportExportModelAdmin):
#     list_display = ("customer", "invoice_name", "invoice_no")
    


@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("invoice", "services_name", "created")


# class ExportMixinAdmin(ExportMixin, admin.ModelAdmin):
    
#     #Choose your format

#     def get_export_formats(self):
#         formats = (
#             base_formats.CSV,
#             base_formats.XLSX,
#             base_formats.TSV,
#             base_formats.ODS,
#             base_formats.JSON,
#             base_formats.HTML,
#           )

#         return [f for f in formats if f().can_export()]

#     class Meta:
#         abstract = True


# class InvoiceResource(resources.ModelResource):
#     customer = Field('name','email','phone_no')
#     class Meta:
#         model = Invoice
#         exclude = ['id']
        
    
#     def get_customer(self, Invoice):
#         return '%s by %s' % (Invoice.customer.name,Invoice.customer.email,Invoice.customer.phone_no)


# class InvoiceAdmin(ExportMixinAdmin):
#     resource_class = InvoiceResource


# admin.site.register(Invoice, InvoiceAdmin)



class InvoiceExcelAdmin(ImportExportModelAdmin):
    list_display = ("customer", "invoice_name", "invoice_no")
    resource_class = InvoiceAdminResource
admin.site.register(Invoice,InvoiceExcelAdmin)