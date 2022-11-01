from . import views
from django.urls import path


app_name = "services"

urlpatterns = [
    path("services-head/", views.serviceHead, name="serviceHead"),
    path('services/<slug:slug>/',views.service,name='service'),
    path("service-details/<slug:slug>/", views.serviceDetails, name="serviceDetails"),
]
