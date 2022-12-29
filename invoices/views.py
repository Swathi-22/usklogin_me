from .forms import CustomerForm
from .forms import InvoiceItemFormset
from .models import Customer
from .models import Invoice
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView


class CustomerList(ListView):
    template_name = "invoice/customer_list.html"

    def get_queryset(self):
        return Customer.objects.filter(created_by=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["is_bill"] = True
        return context


class CustomerCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    template_name = "invoice/customer_form.html"
    success_url = reverse_lazy("invoices:customer-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CustomerUpdate(UpdateView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    fields = ["name", "email", "phone_no"]
    template_name = "invoice/customer_form.html"


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_confirm_delete.html"


class InvoiceList(ListView):
    model = Invoice
    template_name = "invoice/invoice_list.html"


class InvoiceCreate(CreateView):
    model = Invoice
    fields = ["customer", "invoice_name", "invoice_no"]
    template_name = "invoice/invoice_form.html"

    def form_class(self):
        form_class = super().form_class()
        form_class.base_fields["customer"].queryset = Customer.objects.filter(created_by=self.request.user)
        return form_class


class InvoiceUpdate(UpdateView):
    model = Invoice
    fields = ["customer", "invoice_name", "invoice_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"


class InvoiceDelete(DeleteView):
    model = Invoice
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_confirm_delete.html"


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "invoice/general_3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoices"] = self.object
        return context


class CustomerInvoieCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["invoices"] = CustomerForm(self.request.POST or None)
        return data

    def form_valid(self, form):
        invoices = CustomerForm(self.request.POST or None)
        with transaction.atomic():
            self.object = form.save()
            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super().form_valid(form)


class CustomerInvoieUpdate(UpdateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["invoices"] = CustomerForm(self.request.POST or None, instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()
            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super().form_valid(form)


class InvoiceItemCreate(CreateView):
    model = Invoice
    fields = ["customer", "invoice_name", "invoice_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoices_items"] = InvoiceItemFormset(self.request.POST or None)
        return context

    def form_valid(self, form):
        invoices_items = InvoiceItemFormset(self.request.POST or None)
        with transaction.atomic():
            self.object = form.save()
            if invoices_items.is_valid():
                invoices_items.instance = self.object
                invoices_items.save()
        return super().form_valid(form)


class InvoieItemUpdate(UpdateView):
    model = Invoice
    fields = ["customer", "invoice_name", "invoice_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["invoices_items"] = InvoiceItemFormset(self.request.POST or None, instance=self.object)
        return data

    def form_valid(self, form):
        invoices_items = InvoiceItemFormset(self.request.POST or None, instance=self.object)
        with transaction.atomic():
            self.object = form.save()
            if invoices_items.is_valid():
                invoices_items.instance = self.object
                invoices_items.save()
        return super().form_valid(form)
