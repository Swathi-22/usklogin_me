from . import views
from django.urls import path
from django.views.static import serve


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("expired/", views.expired, name="expired"),
    path("start/", views.start, name="start"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("profile-update/", views.profile_update, name="profile_update"),
    path("settings/", views.settings_menu, name="settings"),
    path("notes/", views.notes, name="notes"),
    path("notification/", views.notification, name="notification"),
    path("generate-poster/", views.generate_poster, name="generate_poster"),
    path("generate-bill/", views.generate_bill, name="generate_bill"),
    path("search-invocie/", views.searching_invoice, name="searching_invoice"),
    path("search/", views.search_items, name="search_items"),
    path("generate-form/", views.generate_forms, name="generate_forms"),
    path("download/", serve, {"document_root": "settings.MEDIA_ROOT"}),
    path("documents/", views.documents, name="documents"),
    path("softwares/", views.software, name="software"),
    path("tools/", views.tools, name="tools"),
    path("marketing-tip/", views.marketing_tip, name="marketing_tip"),
    path("other-ideas/", views.other_idea, name="other_idea"),
    path("agency-portal/", views.agency_portal, name="agency_portal"),
    path("back-office-services/", views.back_office_services, name="back_office_services"),
    path("bonus/", views.bonus, name="bonus"),
    path("support/", views.support, name="support"),
    path("support-request/", views.support_request, name="support_request"),
    path("support-ticket/", views.support_ticket, name="support_ticket"),
    path("upgrade-request/", views.upgrade_plan_request, name="upgrade_plan_request"),
    path("FAQ/", views.F_A_Q, name="F_A_Q"),
    path("terms-and-conditions/", views.termsConditions, name="termsConditions"),
    path("call-support/", views.call_support, name="call_support"),
    path("whatsapp-support/", views.whatsapp_support, name="whatsapp_support"),
    path("payment/<str:pk>/", views.order_payment, name="order_payment"),
    path("callback/<str:pk>/", views.callback, name="callback"),
    path("plan_upgrading/", views.upgrade_plan, name="upgrade_plan"),
    path("upgrade-callback/", views.upgrade_callback, name="upgrade_callback"),
    path("download-pdf-certificate/", views.Certificate.as_view(), name="pdf_certificate"),
    path("buynow-branding-image/", views.buy_now_branding_image, name="buy_now_branding_image"),
    path("add-on_services/", views.add_on_services, name="add_on_services"),
    path("newly-addedd-services/", views.newly_added_services, name="newly_added_services"),
    path("important-poster/", views.important_services, name="important_services"),
]
