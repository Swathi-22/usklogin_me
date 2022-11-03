from .forms import CustomerForm
from .forms import InvoiceItemFormset
from .models import Customer
from .models import Invoice, InvoiceItem
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView


class CustomerList(ListView):
    model = Customer
    template_name = "invoice/customer_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["is_bill"] = True
        return context


class CustomerCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    template_name = "invoice/customer_form.html"


class CustomerInvoieCreate(CreateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices"] = CustomerForm(self.request.POST)
        else:
            data["invoices"] = CustomerForm()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieCreate, self).form_valid(form)


class CustomerUpdate(UpdateView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    fields = ["name", "email", "phone_no"]
    template_name = "invoice/customer_form.html"


class CustomerInvoieUpdate(UpdateView):
    model = Customer
    fields = ["name", "email", "phone_no", "address"]
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_form.html"

    def get_context_data(self, **kwargs):
        data = super(CustomerInvoieUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices"] = CustomerForm(self.request.POST, instance=self.object)
        else:
            data["invoices"] = CustomerForm(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices = context["invoices"]
        with transaction.atomic():
            self.object = form.save()

            if invoices.is_valid():
                invoices.instance = self.object
                invoices.save()
        return super(CustomerInvoieUpdate, self).form_valid(form)


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy("invoices:customer-list")
    template_name = "invoice/customer_confirm_delete.html"

    ### invoice items create ###


class InvoiceList(ListView):
    model = Invoice
    template_name = "invoice/invoice_list.html"


class InvoiceCreate(CreateView):
    model = Invoice
    fields = ["customer", "invoice_name", "from_address", "invoice_no", "phone_no"]
    template_name = "invoice/invoice_form.html"


class InvoiceItemCreate(CreateView):
    model = Invoice
    fields = ["customer", "invoice_name", "from_address", "invoice_no", "phone_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"

    def get_context_data(self, **kwargs):
        context = super(InvoiceItemCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context["invoices_items"] = InvoiceItemFormset(self.request.POST)
        else:
            context["invoices_items"] = InvoiceItemFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        invoices_items = context["invoices_items"]
        with transaction.atomic():
            self.object = form.save()

            if invoices_items.is_valid():
                invoices_items.instance = self.object
                invoices_items.save()
        return super(InvoiceItemCreate, self).form_valid(form)


class InvoiceUpdate(UpdateView):
    model = Invoice
    fields = ["customer", "invoice_name", "from_address", "invoice_no", "phone_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"


class InvoieItemUpdate(UpdateView):
    model = Invoice
    fields = ["customer", "invoice_name", "from_address", "invoice_no", "phone_no"]
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_form.html"

    def get_context_data(self, **kwargs):
        data = super(InvoieItemUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data["invoices_items"] = InvoiceItemFormset(self.request.POST, instance=self.object)
        else:
            data["invoices_items"] = InvoiceItemFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        invoices_items = context["invoices_items"]
        with transaction.atomic():
            self.object = form.save()

            if invoices_items.is_valid():
                invoices_items.instance = self.object
                invoices_items.save()
        return super(InvoieItemUpdate, self).form_valid(form)


class InvoiceDelete(DeleteView):
    model = Invoice
    success_url = reverse_lazy("invoices:invoice-list")
    template_name = "invoice/invoice_confirm_delete.html"


class InvoiceDetailView(DetailView):
    model = InvoiceItem
    template_name = "invoice/general_3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoices"] = self.object
        return context
