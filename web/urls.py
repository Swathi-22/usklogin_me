from . import views
from django.urls import path
from django.views.static import serve


app_name = "web"

urlpatterns = [
    # path("", views.login_view, name="login_view"),
    path("app/", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("change-password/<token>/", views.change_password, name="change_password"),
    path("profile/", views.profile, name="profile"),
    path("profile-update/", views.profile_update, name="profile_update"),
    path("settings/", views.settings_menu, name="settings"),
    path("notes/", views.notes, name="notes"),
    path("notification/", views.notification, name="notification"),
    path("generate-poster/", views.generatePoster, name="generatePoster"),
    path("generate-bill/", views.generateBill, name="generateBill"),
    path("search-invocie/", views.searching_invoice, name="searching_invoice"),
    path("search/", views.search_items, name="search_items"),
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
    path("call-support/", views.call_support, name="call_support"),
    path("whatsapp-support/", views.whatsapp_support, name="whatsapp_support"),
    # path("upgrade-plan/", views.upgrade_plan, name="upgrade_plan"),
    path("payment/<str:pk>/", views.order_payment, name="order_payment"),
    path("upgrade_plan/", views.upgrade_plan, name="upgrade_plan"),
    path("callback/", views.callback, name="callback"),
    path("download-certificate/", views.certificate_view, name="certificate_view"),
    path("download-pdf-certificate/", views.Certificate.as_view(), name="pdf_certificate"),
    # path('download-certificate-download/', PDFView.as_view(template_name="web/certificate.html"),name="certificate"),
    # path("logout/", views.logout_view, name="logout"),
    # path("test/", views.test, name="test"),
]
