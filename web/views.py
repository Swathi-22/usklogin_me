import json
import os
from itertools import chain

from accounts.forms import UserRegistrationForm
from accounts.models import User
from invoices.models import InvoiceItem
from invoices.models import Invoice
from services.models import BrandingImage
from services.models import ServiceHeads
from services.models import Services
from web.models import FAQ
from web.models import AddonServices
from web.models import AgencyPortal
from web.models import AgencyPortalService
from web.models import AgentBonus
from web.models import BackOfficeServices
from web.models import CallSupport
from web.models import CommonServicesPoster
from web.models import DownloadDocuments
from web.models import DownloadForms
from web.models import FestivelPoster
from web.models import ImportantPoster
from web.models import LatestNews
from web.models import MarketingTips
from web.models import NewServicePoster
from web.models import OnloadPopup
from web.models import Order
from web.models import OtherIdeas
from web.models import Others
from web.models import PaymentStatus
from web.models import ProfessionalPoster
from web.models import PromotionalPoster
from web.models import SeasonalService
from web.models import Softwares
from web.models import Subscription
from web.models import Tools
from web.models import UpdatesorInformation
from web.models import WhatsappSupport

import razorpay
from .decorators import subscription_required
from .forms import BrandingImageForm
from .forms import SupportRequestForm
from .forms import SupportTicketForm
from .forms import UserUpdateForm
from .utils import PDFView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render 
from django.shortcuts import get_object_or_404

from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from registration.views import RegistrationView


# function
def verify_signature(response_data):
    client = razorpay.Client(auth=(settings.RAZOR_PAY_KEY, settings.RAZOR_PAY_SECRET))
    return client.utility.verify_payment_signature(response_data)


def order_payment(request):
    user = request.user
    amount = 1499
    client = razorpay.Client(auth=(settings.RAZOR_PAY_KEY, settings.RAZOR_PAY_SECRET))
    razorpay_order = client.order.create({"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
    order, created = Order.objects.get_or_create(user=user, amount=amount, provider_order_id=razorpay_order["id"])
    context = {"order": order, "amount": amount, "razorpay_key": settings.RAZOR_PAY_KEY, "razorpay_order": razorpay_order, "callback_url": f"{settings.DOMAIN}/callback/"}
    return render(request, "web/payment.html", context)


@csrf_exempt
def callback(request):
    user = request.user
    amount = 1499
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        response_data = {"razorpay_order_id": provider_order_id, "razorpay_payment_id": payment_id, "razorpay_signature": signature_id}
        print(response_data)

        if verify_signature(response_data):
            print("Signature verification successful")
            order, _ = Order.objects.get_or_create(user=user, provider_order_id=provider_order_id)
            order_status = PaymentStatus.SUCCESS
            order.status = PaymentStatus.SUCCESS
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()

            subscriptions = Subscription.objects.create(user=request.user, status="Success", types="Access", valid_upto=valid_from + timedelta(days=365), amount=amount)

            # email = order.user.email
            # phone = order.user.phone
            # subject = "Registration Completed on USKLOGIN.COM"
            # message = f"""
            #     Welcome to USKLOGIN.COM...Thank you for registered on USKLOGIN.COM.
            #     Use this username and password to login.

            #     Username: {phone}
            #     Password: {password}
            # """
            # send_mail(subject, message, "websiteusk@gmail.com", [email], fail_silently=False)
            # subject = "Registration Completed on USKLOGIN.COM"
            # message = f"""
            #     One more Agent on USKLOGIN.COM

            #     Username: {phone}
            #     Password: {password}
            # """
        else:
            print("Signature verification failed, please check the secret key")
            order_status = PaymentStatus.FAILURE
        return render(request, "web/callback.html", context={"status": order_status, "subscriptions": subscriptions})
    else:
        context = {"status": PaymentStatus.FAILURE}
        return render(request, "web/payment.html", context)


@login_required
@subscription_required
def upgrade_plan(request):
    user = request.user
    amount = 500
    client = razorpay.Client(auth=(settings.RAZOR_PAY_KEY, settings.RAZOR_PAY_SECRET))
    razorpay_order = client.order.create({"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
    order, created = Subscription.objects.get_or_create(user=user, amount=amount, provider_order_id=razorpay_order["id"])
    subscriptions = Subscription.objects.filter(user=request.user, status="Success", types="Support")
    context = {"order": order, "amount": amount, "razorpay_key": settings.RAZOR_PAY_KEY, "razorpay_order": razorpay_order, "callback_url": f"{settings.DOMAIN}/upgrade_callback/"}
    return render(request, "web/payment.html", context)


@csrf_exempt
@login_required
@subscription_required
def upgrade_callback(request):
    user = request.user
    amount = 500
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        response_data = {"razorpay_order_id": provider_order_id, "razorpay_payment_id": payment_id, "razorpay_signature": signature_id}
        print(response_data)

        if verify_signature(response_data):
            order, _ = Subscription.objects.get_or_create(user=user, provider_order_id=provider_order_id)
            order_status = PaymentStatus.SUCCESS
            order.status = PaymentStatus.SUCCESS
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()

            subscriptions = Subscription.objects.create(user=request.user, status="Success", types="Support",valid_upto=valid_from + timedelta(days=30), amount=amount)

            email = order.user.email
            subject = "Upgrade Plan"
            message = "The scheduled upgrade has been completed successfully."
            send_mail(subject, message, "websiteusk@gmail.com", [email], fail_silently=False)
            print("Payment Successful")
            messages.success(request, "Payment Successful")
        else:
            order_status = PaymentStatus.FAILURE
        return render(request, "web/planupgrade-callback.html", context={"status": order_status, "subscriptions": subscriptions})
    else:
        context = {"status": PaymentStatus.FAILURE}
        return render(request, "web/payment.html", context)


# verified views


def start(request):
    if request.method == "POST":
        mobile = request.POST.get("mobile", None)
        if mobile:
            if User.objects.filter(username=mobile).exists():
                return redirect("auth_login")
            else:
                return redirect("web:register")
    else:
        if request.user.is_authenticated:
            return redirect("web:index")
    return render(request, "web/start.html")


class AuthRegistrationView(RegistrationView):
    form_class = UserRegistrationForm

    def register(self, form):
        form = self.form_class(self.request.POST)
        username = self.request.POST.get("phone")
        if User.objects.filter(username=username).exists():
            messages.error(self.request, "User already exists!")
            return redirect("auth_login")
        else:
            if form.is_valid():
                data = form.save(commit=False)
                data.username = self.request.POST.get("phone")
                data.save()
                messages.success(self.request, "You have successfully registered!")
                return redirect("web:order_payment")
            else:
                messages.error(self.request, "Invalid form")
                return redirect("auth_login")

    def get_success_url(self, user=None):
        return "/app/login/"


# website pageviews


def upgrade_plan_request(request):
    context = {}
    return render(request, "web/upgrade-request.html", context)


def expired(request):
    return render(request, "web/expired.html")


@csrf_exempt
@login_required
@subscription_required
def profile(request):
    user_form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
    instance = BrandingImage.objects.filter(user=request.user)
    branding_image_form = BrandingImageForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if branding_image_form.is_valid():
            data = branding_image_form.save(commit=False)
            data.user = request.user
            data.save()
            subject = "Need To Verify Branding Image "
            message = f"""
                Username: {request.user.phone}
                Userid: {request.user.id}, Added a branding image. Please verify the branding image.
            """
            send_mail(subject, message, "websiteusk@gmail.com", ["uskdemomail@gmail.com"], fail_silently=False)
            print("done")
        else:
            print(branding_image_form.errors)
    uploaded_branding_image = BrandingImage.objects.filter(user=request.user).last()
    subscription_validity = Subscription.objects.filter(user=request.user).last()
    order_validity = Order.objects.filter(user=request.user).last()

    context = {
        "is_profile": True,
        "user_form": user_form,
        "branding_image_form": branding_image_form,
        "instance": instance,
        "order_validity": order_validity,
        "uploaded_branding_image": uploaded_branding_image,
        "subscription_validity": subscription_validity,
    }
    return render(request, "web/profile.html", context)


class Certificate(PDFView, LoginRequiredMixin):
    template_name = "web/certificate-pdf.html"
    pdfkit_options = {"page-height": "8.5in", "page-width": "11in", "encoding": "UTF-8", "margin-top": "0", "margin-bottom": "0", "margin-left": "0", "margin-right": "0"}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["logged_user"] = self.request.user
        context["content"] = self.request.user.name
        context["shop_name"] = self.request.user.shop_name
        context["district"] = self.request.user.district
        context["pincode"] = self.request.user.pincode
        context["created"] = self.request.user.created
        context["id"] = self.request.user.id
        return context


@login_required
@subscription_required
def profile_update(request):
    user_form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
    context = {"user_form": user_form}
    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
            return redirect("web:profile")
    return render(request, "web/profile-update.html", context)


def settings_menu(request):
    context = {}
    return render(request, "web/settings.html", context)


@login_required
@subscription_required
def index(request):
    service_head = ServiceHeads.objects.all()[:12]
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all().order_by("-id")[0:2]
    important_poster = ImportantPoster.objects.all().order_by("-id")[0:2]
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    on_load_popup = OnloadPopup.objects.all().order_by("-id")
    context = {
        "is_index": True,
        "service_head": service_head,
        "latest_news": latest_news,
        "new_service_poster": new_service_poster,
        "important_poster": important_poster,
        "room_name": "broadcast",
        "branding_image": branding_image,
        "room_name": "broadcast",
        "on_load_popup": on_load_popup,
    }
    return render(request, "web/index.html", context)


@login_required
@subscription_required
def notes(request):
    context = {"room_name": "broadcast"}
    return render(request, "web/notes.html", context)


def notification(request):
    # channel_layer = get_channel_layer()
    # async_to_sync(channel_layer.group_send)("notification_broadcast", {"type": "send_notification", "message": json.dumps("Notification")})
    return HttpResponse("Done")


@login_required
@subscription_required
def generate_poster(request):
    recently_common_services_poster = CommonServicesPoster.objects.all().order_by("-id")[0:2]
    recently_festivel_poster = FestivelPoster.objects.all().order_by("-id")[0:2]
    recently_professional_poster = ProfessionalPoster.objects.all().order_by("-id")[0:2]
    recently_new_service_poster = NewServicePoster.objects.all().order_by("-id")[0:2]
    recently_agency_portal_services = AgencyPortalService.objects.all().order_by("-id")[0:2]
    recently_seasonal_service = SeasonalService.objects.all().order_by("-id")[0:2]
    recently_updates_or_information = UpdatesorInformation.objects.all().order_by("-id")[0:2]
    recently_promotional_poster = PromotionalPoster.objects.all().order_by("-id")[0:2]
    recently_others = Others.objects.all().order_by("-id")[0:2]
    common_services_poster = CommonServicesPoster.objects.all()
    festivel_poster = FestivelPoster.objects.all()
    professional_poster = ProfessionalPoster.objects.all()
    new_service_poster = NewServicePoster.objects.all()
    agency_portal_services = AgencyPortalService.objects.all()
    seasonal_service = SeasonalService.objects.all()
    updates_or_information = UpdatesorInformation.objects.all()
    promotional_poster = PromotionalPoster.objects.all()
    others = Others.objects.all()
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    context = {
        "is_poster": True,
        "common_services_poster": common_services_poster,
        "festivel_poster": festivel_poster,
        "professional_poster": professional_poster,
        "branding_image": branding_image,
        "room_name": "broadcast",
        "recently_common_services_poster": recently_common_services_poster,
        "recently_festivel_poster": recently_festivel_poster,
        "recently_professional_poster": recently_professional_poster,
        "new_service_poster": new_service_poster,
        "recently_new_service_poster": recently_new_service_poster,
        "recently_agency_portal_services": recently_agency_portal_services,
        "recently_seasonal_service": recently_seasonal_service,
        "recently_updates_or_information": recently_updates_or_information,
        "recently_promotional_poster": recently_promotional_poster,
        "recently_others": recently_others,
        "agency_portal_services": agency_portal_services,
        "seasonal_service": seasonal_service,
        "updates_or_information": updates_or_information,
        "promotional_poster": promotional_poster,
        "others": others,
    }
    return render(request, "web/generate-poster.html", context)


@csrf_exempt
@login_required
@subscription_required
def search_items(request):
    if request.POST:
        search_Key = request.POST["search_Key"]
        services = Services.objects.select_related("service_head").filter(Q(service_head__title__icontains=search_Key) | Q(title__icontains=search_Key))
        new_service_poster = NewServicePoster.objects.filter(Q(title__icontains=search_Key))
        important_poster = ImportantPoster.objects.filter(Q(title__icontains=search_Key))
        common_services_poster = CommonServicesPoster.objects.filter(Q(title__icontains=search_Key))
        festivel_poster = FestivelPoster.objects.filter(Q(title__icontains=search_Key))
        professional_poster = ProfessionalPoster.objects.filter(Q(title__icontains=search_Key))
        branding_image = BrandingImage.objects.filter(user=request.user).last()
        result = chain(services, new_service_poster, important_poster, common_services_poster, festivel_poster, professional_poster)
        print(services.count())
        context = {}
        context["template"] = render_to_string("web/service-searching.html", {"result": result, "branding_image": branding_image}, request=request)
    return JsonResponse(context)


@login_required
@subscription_required
def generate_bill(request):
    services = Services.objects.all()
    context = {"is_bill": True, "services": services, "room_name": "broadcast"}
    return render(request, "web/generate-bill.html", context)


@csrf_exempt
@login_required
@subscription_required
def searching_invoice(request):
    search = ""
    invoice = ""
    invoice_item  = ""
    if "search" in request.GET:
        search = request.GET["search"]
        invoice = Invoice.objects.get(customer__phone_no__icontains=search)
        invoice_item = InvoiceItem.objects.filter(invoice=invoice)
<<<<<<< HEAD
        context = {"invoice": invoice,"invoice_item":invoice_item,"status":1}
        return render(request, "web/invoice-searching.html", context)
    context = {"is_search": True, "invoice": invoice,"invoice_item":invoice_item}
    return render(request, "web/invoice-searching.html")
    


# @csrf_exempt
# @login_required
# @subscription_required
# def searching_invoice(request):
#     search = ""
#     invoice = ""
#     if "search" in request.GET:
#         search = request.GET["search"]
#         invoice = InvoiceItem.objects.filter(invoice__customer__phone_no__icontains=search)
#     else:
#         invoice = InvoiceItem.objects.filter(invoice__customer__created_by=request.user)
#     context = {"is_search": True, "invoice": invoice}
#     return render(request, "web/invoice-searching.html", context)
#     return JsonResponse(context)



@login_required
@subscription_required
def invoice_search_print(request,pk):
    invoice = get_object_or_404(Invoice,pk=pk)
    invoice_item=InvoiceItem.objects.filter(invoice=invoice)
    context = {"invoice":invoice,"invoice_item":invoice_item,}
    return render(request,'web/invoice-search-print.html',context)

=======
        context = {"invoice": invoice,"invoice_item":invoice_item}
    else:
        invoice = Invoice.objects.filter(customer__created_by=request.user)
        context = {"invoice": invoice,}
    context = {"is_search": True, "invoice": invoice,"invoice_item":invoice_item}
    return render(request, "web/invoice-searching.html", context)
    return JsonResponse(context)
>>>>>>> 57499aa069832df16ec9462e4c4a3c67908c7236


# @csrf_exempt
# @login_required
# @subscription_required
# def searching_invoice(request):
#     search = ""
#     invoice = ""
#     if "search" in request.GET:
#         search = request.GET["search"]
#         invoice = InvoiceItem.objects.filter(invoice__customer__phone_no__icontains=search)
#     else:
#         invoice = InvoiceItem.objects.filter(invoice__customer__created_by=request.user)
#     context = {"is_search": True, "invoice": invoice}
#     return render(request, "web/invoice-searching.html", context)
#     return JsonResponse(context)



@login_required
@subscription_required
def invoice_search_print(request,pk):
    print(pk)
    invoice = InvoiceItem.objects.filter(invoice__customer=pk)
    invoices = InvoiceItem.objects.filter(invoice__customer=pk).last()
    print(invoice)
    context = {"invoice":invoice,"invoices":invoices}
    return render(request,'web/invoice-search-print.html',context)



@login_required
@subscription_required
def generate_forms(request):
    village_services_related = DownloadForms.objects.filter(category="Village Services Related")
    panchayath_related = DownloadForms.objects.filter(category="Panchayath Related")
    student_related = DownloadForms.objects.filter(category="Students Related")
    pension_scheme_related = DownloadForms.objects.filter(category="Pension Scheme Related")
    income_tax_department = DownloadForms.objects.filter(category="Income Tax Department")
    others = DownloadForms.objects.filter(category="Others")
    context = {
        "is_form": True,
        "room_name": "broadcast",
        "village_services_related": village_services_related,
        "panchayath_related": panchayath_related,
        "student_related": student_related,
        "pension_scheme_related": pension_scheme_related,
        "pension_scheme_related": pension_scheme_related,
        "income_tax_department": income_tax_department,
        "others": others,
    }
    return render(request, "web/generate-form.html", context)


@login_required
@subscription_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response["Content-Disposition"] = "inline;filename=" + os.path.basename(file_path)
            return response
    raise Http404


@login_required
@subscription_required
def documents(request):
    cv_format = DownloadDocuments.objects.filter(category="CV Formats")
    agreement_model = DownloadDocuments.objects.filter(category="Agreement Models")
    business_related = DownloadDocuments.objects.filter(category="Business Related")
    others = DownloadDocuments.objects.filter(category="Others")
    context = {"is_document": True, "room_name": "broadcast", "cv_format": cv_format, "agreement_model": agreement_model, "business_related": business_related, "others": others}
    return render(request, "web/documents.html", context)


@login_required
@subscription_required
def software(request):
    softwares = Softwares.objects.all()
    context = {"is_software": True, "softwares": softwares, "room_name": "broadcast"}
    return render(request, "web/softwares.html", context)


@login_required
@subscription_required
def tools(request):
    tools = Tools.objects.all()
    context = {"is_tool": True, "tools": tools, "room_name": "broadcast"}
    return render(request, "web/tools.html", context)


@login_required
@subscription_required
def marketing_tip(request):
    marketing_tips = MarketingTips.objects.all()
    context = {"is_tip": True, "marketing_tips": marketing_tips, "room_name": "broadcast"}
    return render(request, "web/marketing-tip.html", context)


@login_required
@subscription_required
def other_idea(request):
    other_ideas = OtherIdeas.objects.all()
    context = {"is_idea": True, "other_ideas": other_ideas, "room_name": "broadcast"}
    return render(request, "web/other-ideas.html", context)


@login_required
@subscription_required
def agency_portal(request):
    agency_portal = AgencyPortal.objects.all()
    context = {"is_portal": True, "agency_portal": agency_portal, "room_name": "broadcast"}
    return render(request, "web/agency-portal.html", context)


@login_required
@subscription_required
def back_office_services(request):
    back_office_services = BackOfficeServices.objects.all()
    context = {"is_backservice": True, "back_office_services": back_office_services, "room_name": "broadcast"}
    return render(request, "web/back-office-services.html", context)


@login_required
@subscription_required
def bonus(request):
    agent_bonus = AgentBonus.objects.all()
    context = {"is_bonus": True, "agent_bonus": agent_bonus, "room_name": "broadcast"}
    return render(request, "web/bonus.html", context)


@login_required
@subscription_required
def support(request):
    request.user
    context = {"is_support": True, "room_name": "broadcast"}
    return render(request, "web/support.html", context)


@login_required
@subscription_required
def support_request(request):
    forms = SupportRequestForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {"status": "true", "title": "Successfully Submitted", "message": "Message successfully submitted"}
        else:
            response_data = {"status": "false", "title": "Form validation error", "message": repr(forms.errors)}
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    context = {"forms": forms, "room_name": "broadcast"}
    return render(request, "web/support-request.html", context)


@login_required
@subscription_required
def F_A_Q(request):
    Frequently_Asked_Questions = FAQ.objects.all()
    context = {"Frequently_Asked_Questions": Frequently_Asked_Questions, "room_name": "broadcast"}
    return render(request, "web/faq.html", context)


@login_required
@subscription_required
def support_ticket(request):
    forms = SupportTicketForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {"status": "true", "title": "Successfully Submitted", "message": "Message successfully submitted"}
        else:
            response_data = {"status": "false", "title": "Form validation error", "message": repr(forms.errors)}
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    context = {"forms": forms, "room_name": "broadcast"}
    return render(request, "web/support-ticket.html", context)


@login_required
@subscription_required
def call_support(request):
    call_support = CallSupport.objects.all()
    context = {"call_support": call_support}
    return render(request, "web/call-support.html", context)


@login_required
@subscription_required
def whatsapp_support(request):
    whatsapp_support = WhatsappSupport.objects.all()
    context = {"whatsapp_support": whatsapp_support}
    return render(request, "web/whatsapp-support.html", context)


def terms_and_conditions(request):
    context = {}
    return render(request, "web/terms&conditions.html", context)


@login_required
@subscription_required
def certificate_view(request):
    context = {"logined_user": request.user}
    return render(request, "web/certificate.html", context)


@login_required
@subscription_required
def buy_now_branding_image(request):
    context = {}
    return render(request, "web/buy-now.html", context)


@login_required
@subscription_required
def add_on_services(request):
    addon_services = AddonServices.objects.all()
    context = {"addon_services": addon_services}
    return render(request, "web/add-on-services.html", context)


@login_required
@subscription_required
def newly_added_services(request):
    service_posters = NewServicePoster.objects.all()
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    context = {"service_posters": service_posters, "branding_image": branding_image}
    return render(request, "web/newly-addedd-services.html", context)


@login_required
@subscription_required
def important_services(request):
    important_posters = ImportantPoster.objects.all()
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    context = {"important_posters": important_posters, "branding_image": branding_image}
    return render(request, "web/important-posters.html", context)


