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
        fields = ("customer", "invoice_name", "invoice_no")


class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ("invoice", "services_name", "services_charge", "username", "password", "descripton", "qty")
        widgets = {
            "services_name": widgets.Select(attrs={"class": "form-control"}),
            "services_charge": widgets.NumberInput(attrs={"class": "form-control"}),
            "username": widgets.TextInput(attrs={"class": "form-control"}),
            "password": widgets.TextInput(attrs={"class": "form-control"}),
            "descripton": widgets.Textarea(attrs={"class": "form-control"}),
            "qty": widgets.NumberInput(attrs={"class": "form-control"}),
        }


InvoiceItemFormset = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, exclude=("created",), extra=1, can_delete=False)
