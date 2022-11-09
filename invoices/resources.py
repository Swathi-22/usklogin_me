from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import Invoice,Customer



class InvoiceAdminResource(resources.ModelResource):
    customer_name = fields.Field(column_name='name', attribute='name', widget=ForeignKeyWidget(Customer, field='name'))
    customer_email = fields.Field(column_name='email', attribute='email', widget=ForeignKeyWidget(Customer, field='email'))
    customer_phone_no = fields.Field(column_name='phone_no', attribute='phone_no', widget=ForeignKeyWidget(Customer, field='phone_no'))
   

    class Meta:
        model = Invoice
        fields = ('customer_name','customer_email','customer_phone_no','invoice_name','invoice_no','created' )