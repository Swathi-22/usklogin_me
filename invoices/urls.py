from . import views
from django.urls import path


app_name = "invoices"

urlpatterns = [
    path("customers/", views.CustomerList.as_view(), name="customer-list"),
    path("customers/add/", views.CustomerInvoieCreate.as_view(), name="customer-add"),
    path("customers/update/<int:pk>", views.CustomerInvoieUpdate.as_view(), name="customer-update"),
    path("customers/delete/<int:pk>", views.CustomerDelete.as_view(), name="customer-delete"),
    # invoices
    path("invoice/", views.InvoiceList.as_view(), name="invoice-list"),
    path("invoice/add/", views.InvoiceItemCreate.as_view(), name="invoice-add"),
    path("invoice/update/<int:pk>", views.InvoieItemUpdate.as_view(), name="invoice-update"),
    path("invoice/delete/<int:pk>", views.InvoiceDelete.as_view(), name="invoice-delete"),
    # #### Download invoices  ###
    path("invoice/download/<int:pk>", views.InvoiceDetailView.as_view(), name="invoice_download"),
]
