from . import views
from django.urls import path
from django.views.static import serve


app_name = "web"
    
urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("register/", views.register, name="register"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("change-password/<token>/", views.change_password, name="change_password"),
    path("profile/", views.profile, name="profile"),
    path("profile-update/", views.profile_update, name="profile_update"),
    path("settings/", views.settings, name="settings"),
    path("dashboard/", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notification/", views.notification, name="notification"),
    path("generate-poster/", views.generatePoster, name="generatePoster"),
    path("generate-bill/", views.generateBill, name="generateBill"),
    path("search/", views.search_items,name="search_items"),
    path("invoice/", views.invoice, name="invoice"),
    path("generate-form/", views.generateForms, name="generateForms"),
    path("download/", serve, {"document_root": "settings.MEDIA_ROOT"}),
    path("documents/", views.documents, name="documents"),
    path("softwares/", views.software, name="software"),
    path("tools/", views.tools, name="tools"),
    path("marketing-tip/", views.marketingTip, name="marketingTip"),
    path("other-ideas/", views.otherIdea, name="otherIdea"),
    path("agency-portal/", views.agencyPortal, name="agencyPortal"),
    path("back-office-services/", views.backOfficeServices, name="backOfficeServices"),
    path("bonus/", views.bonus, name="bonus"),
    path("support/", views.support, name="support"),
    path("support-request/", views.supportRequest, name="supportRequest"),
    path("support-ticket/", views.supportTicket, name="supportTicket"),
    path("FAQ/", views.F_A_Q, name="F_A_Q"),
    path("terms-and-conditions/", views.termsConditions, name="termsConditions"),
    path("payment/", views.order_payment, name="payment"),
    path("callback/", views.callback, name="callback"),
    path("logout/", views.logout, name="logout"),
]
