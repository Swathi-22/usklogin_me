from .models import Customer
from .models import Invoice
from import_export import fields
from import_export import resources
from import_export.widgets import ForeignKeyWidget


class InvoiceAdminResource(resources.ModelResource):
    customer_name = fields.Field(column_name="customer_name", attribute="customer", widget=ForeignKeyWidget(Customer, "name"))
    customer_email = fields.Field(column_name="customer_email", attribute="customer", widget=ForeignKeyWidget(Customer, "email"))
    customer_phone_no = fields.Field(column_name="customer_phone_no", attribute="customer", widget=ForeignKeyWidget(Customer, "phone_no"))
    customer_address = fields.Field(column_name="customer_address", attribute="customer", widget=ForeignKeyWidget(Customer, "address"))

    class Meta:
        model = Invoice
        fields = ("customer_name", "customer_email", "customer_phone_no", "customer_address", "invoice_name", "invoice_no", "created")
