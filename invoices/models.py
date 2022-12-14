from decimal import Decimal

from accounts.models import User
from services.models import Services

from django.db import models
from django.urls import reverse
from django.utils import timezone
from num2words import num2words

# Create your models here.
class Customer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def get_absolute_url(self):
        return reverse("invoices:customer-update", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_name = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def get_invoiceitem(self):
        return InvoiceItem.objects.filter(invoice=self)

    def get_total(self):
        total = 0
        for item in InvoiceItem.objects.filter(invoice=self):
            total += item.sub_total
        return Decimal(total) if total else 0


    def get_total_in_words(self):
        total = 0
        for item in InvoiceItem.objects.filter(invoice=self):
            total += item.sub_total
        return num2words(total) if total else 0
        

    def get_absolute_url(self):
        return reverse("invoices:invoice-update", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.invoice_name)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    services_name = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="invoices_items")
    services_charge = models.CharField(max_length=100)
    sub_total = models.PositiveIntegerField("Sub Total", blank=True, editable=False)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    fees = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Invoice Item"
        verbose_name_plural = "Invoice Items"

    def get_absolute_url(self):
        return reverse("invoices:invoice_download", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.services_name)

    def save(self, *args, **kwargs):
        self.sub_total = float(self.services_charge) + float(self.fees)
        super().save(*args, **kwargs)
