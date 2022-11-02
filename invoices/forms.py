from .models import Customer
from .models import Invoice
from .models import InvoiceItem
from django.forms import ModelForm
from django.forms import inlineformset_factory
from django.forms import widgets


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "email", "phone_no", "address")
        exclude = ("created_date",)


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ("customer", "invoice_name", "invoice_no", "from_address", "phone_no")


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ("invoice", "services_name", "services_charge", "username", "password", "descripton", "qty")
        widgets = {
            "services_name": widgets.Select(attrs={"class": "tm_width_3"}),
            "services_charge": widgets.NumberInput(attrs={"class": "tm_width_2"}),
            "username": widgets.TextInput(attrs={"class": "tm_width_3"}),
            "password": widgets.TextInput(attrs={"class": "tm_width_3"}),
            "descripton": widgets.Textarea(attrs={"class": "form-control"}),
            "qty": widgets.NumberInput(attrs={"class": "tm_width_1"}),
        }


InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, exclude=("created",), extra=1, can_delete=False)
