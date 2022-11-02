from services.models import Services

from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def get_absolute_url(self):
        return reverse("customer-update", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.name)


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_name = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    from_address = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    phone_no = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def get_absolute_url(self):
        return reverse("invoice-update", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.invoice_name)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    services_name = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="Services")
    services_charge = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    qty = models.PositiveIntegerField("Quantity")
    created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "InvoiceItem"
        verbose_name_plural = "InvoiceItems"

    def __str__(self):
        return str(self.services_name)
