import json
import os
import uuid
from itertools import chain
from accounts.models import User
from invoices.models import Invoice
from invoices.models import InvoiceItem
from services.models import BrandingImage
from services.models import ServiceHeads
from services.models import Services
from web.models import FAQ
from web.models import AgencyPortal
from django.shortcuts import get_object_or_404
from web.models import AgentBonus
from web.models import BackOfficeServices
from web.models import CallSupport
from web.models import ChangePassword
from web.models import CommonServicesPoster
from web.models import DownloadDocuments
from web.models import DownloadForms
from web.models import FestivelPoster
from web.models import ImportantPoster
from web.models import LatestNews
from web.models import MarketingTips
from web.models import NewServicePoster
from web.models import Order
from web.models import OtherIdeas
from web.models import PaymentStatus
from web.models import ProfessionalPoster
from web.models import Softwares
from web.models import Subscription
from web.models import Tools
from web.models import WhatsappSupport
import razorpay
from .forms import BrandingImageForm
# from .forms import BrandingImageUploadingForm
from .forms import SupportRequestForm
from .forms import SupportTicketForm
from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .functions import generate_pw
from .helper import send_forget_password_mail
from .helper import upgrade_reminder_mail
from .utils import PDFView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
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
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


RAZOR_PAY_KEY = "rzp_test_gmilUW5MZmHsEK"
RAZOR_PAY_SECRET = "z7rD3fi8O6rS8vsVMRvmbGkW"


def start(request):
    if request.method == "POST":
        mobile = request.POST.get("mobile", None)
        if mobile:
            if User.objects.filter(username=mobile).exists():
                return redirect("auth_login")
            else:
                return redirect("web:register")
    return render(request, "web/start.html")


def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    temp_pass = generate_pw()
    print(temp_pass)
    context = {"user_form": user_form}
    if request.method == "POST":
        if user_form.is_valid():
            data = user_form.save(commit=False)
            data.username = request.POST.get("phone")
            data.is_active = False
            data.temp_password = temp_pass
            data.set_password(temp_pass)
            data.save()
            messages.success(request, "You have successfully registered!")
            return redirect("web:order_payment", pk=data.pk)
    return render(request, "web/register.html", context)


def order_payment(request, pk):
    user = get_object_or_404(User, id=pk)
    amount = 200
    client = razorpay.Client(auth=(RAZOR_PAY_KEY, RAZOR_PAY_SECRET))
    razorpay_order = client.order.create({"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
    order, created = Order.objects.get_or_create(user=user, amount=amount, provider_order_id=razorpay_order["id"])
    context = {"order": order, "amount": amount, "razorpay_key": RAZOR_PAY_KEY,
               "razorpay_order": razorpay_order, "callback_url": settings.DOMAIN + "/callback/" + pk}
    return render(request, "web/payment.html", context)


@csrf_exempt
def callback(request, pk):
    user = get_object_or_404(User, id=pk)
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        response_data = {"razorpay_order_id": provider_order_id, "razorpay_payment_id": payment_id, "razorpay_signature": signature_id}
        print(response_data)

        if verify_signature(response_data):
            order, _ = Order.objects.get_or_create(user=user, amount=amount, provider_order_id=provider_order_id)
            order_status = PaymentStatus.SUCCESS
            order.status = PaymentStatus.SUCCESS
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()

            order.user.is_active = True
            order.user.save()

            email = order.user.email
            phone = order.user.phone
            password = order.user.temp_password
            subject = "Registration Completed on USKLOGIN.COM"
            message = f"""
                Welcome to USKLOGIN.COM...Thank you for registered on USKLOGIN.COM.
                Use this username and password to login.

                Username: {phone}
                Password: {password}
            """
            send_mail(subject, message, "loginusk@gmail.com", [email], fail_silently=False)
            print("Payment Successful")
            messages.success(request, "Payment Successful")
        else:
            order_status = PaymentStatus.FAILURE
        return render(request, "web/callback.html", context={"status": order_status})
    else:
        return render(request, "web/payment.html")


def test(request):
    user = request.user
    email = "anfasperingavu@gmail.com"
    # upgrade_reminder_mail(user.email, user)
    phone = "1234567890"
    password = "1234567890"
    email = "anfasperingavu@gmail.com"
    subject = "Registration Completed on USKLOGIN.COM"
    message = f"""
        Welcome to USKLOGIN.COM...Thank you for registered on USKLOGIN.COM.
        Use this username and password to login.

        Username: {phone}
        Password: {password}
    """
    send_mail(subject, message, "secure.gedexo@gmail.com", [email], fail_silently=False)
    return HttpResponse("Done")


class Certificate(PDFView, LoginRequiredMixin):
    template_name = "web/certificate-pdf.html"
    pdfkit_options = {"page-height": "8.5in", "page-width": "11in", "encoding": "UTF-8", "margin-top": "0", "margin-bottom": "0", "margin-left": "0", "margin-right": "0"}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["logged_user"] = self.request.user
        context["content"] = "Gedexo Certificate"
        return context


def upgrade_plan(request):
    user = request.user
    amount = 400
    client = razorpay.Client(auth=(RAZOR_PAY_KEY, RAZOR_PAY_SECRET))
    razorpay_order = client.order.create({"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"})
    order, created = Order.objects.get_or_create(user=user, amount=amount, provider_order_id=razorpay_order["id"])
    subscription, created = Subscription.objects.get_or_create(user=user, amount=amount, is_active=True)
    context = {"order": order, "amount": amount, "razorpay_key": RAZOR_PAY_KEY,
               "razorpay_order": razorpay_order, "callback_url": "http://" + "usklogin.geany.website" + "/callback/"}
    return render(request, "web/upgrade_plan.html", context)


def verify_signature(response_data):
    client = razorpay.Client(auth=(RAZOR_PAY_KEY, RAZOR_PAY_SECRET))
    return client.utility.verify_payment_signature(response_data)


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not User.objects.filter(email=email).first():
            messages.warning(request, "User Not Found...")
            return redirect("web:forgot_password")
        user_obj = User.objects.get(email=email)
        token = str(uuid.uuid4())
        ChangePassword.objects.create(user=user_obj, forgot_password_token=token)
        send_forget_password_mail(user_obj.email, token)
        messages.warning(request, "An email is sent")
        return redirect("web:forgot_password")
    context = {}
    return render(request, "web/forgot-password.html", context)


@login_required
def change_password(request, token):
    change_password_obj = ChangePassword.objects.filter(forgot_password_token=token).first()
    if change_password_obj.status:
        messages.warning(request, "Link expired...")
        return redirect("web:forgot_password")
    print(change_password_obj.user.email)
    user_id = User.objects.filter(email=change_password_obj.user.email).first()
    print(change_password_obj)
    if request.method == "POST":
        new_password = request.POST.get("new_pswd")
        confirm_password = request.POST.get("confirm_pswd")
        if user_id is None:
            messages.warning(request, "User not found...")
            return redirect(f"/change-password/{token}/")
        if new_password != confirm_password:
            messages.warning(request, "Your Password and confirm Password dosen't match")
            return redirect(f"/change-password/{token}/")
        user_obj = User.objects.get(email=change_password_obj.user.email)
        user_obj.set_password(new_password)
        user_obj.save()
        ChangePassword.objects.filter(forgot_password_token=token).update(status=True)
        messages.success(request, "Your password is updated")
        return redirect("web:login_view")
    context = {"user_id": change_password_obj.user.id}
    return render(request, "web/change-password.html", context)


@csrf_exempt
@login_required
def profile(request):
    user_form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
    instance, created = BrandingImage.objects.get_or_create(user=request.user)
    branding_image_form = BrandingImageForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST":
        if branding_image_form.is_valid():
            data = branding_image_form.save(commit=False)
            data.user = request.user
            data.save()
        else:
            print(branding_image_form.errors)
    uploaded_branding_image = BrandingImage.objects.get(user=request.user)
    context = {"is_profile": True, "user_form": user_form, "branding_image_form": branding_image_form, 'instance': instance, "uploaded_branding_image": uploaded_branding_image}
    return render(request, "web/profile.html", context)


@login_required
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
def index(request):
    service_head = ServiceHeads.objects.all()
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all()
    important_poster = ImportantPoster.objects.all()
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    context = {
        "is_index": True,
        "service_head": service_head,
        "latest_news": latest_news,
        "new_service_poster": new_service_poster,
        "important_poster": important_poster,
        "room_name": "broadcast",
        "branding_image": branding_image,
        "room_name": "broadcast",
    }
    return render(request, "web/index.html", context)


@login_required
def notes(request):
    context = {"room_name": "broadcast"}
    return render(request, "web/notes.html", context)


def notification(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notification_broadcast", {"type": "send_notification", "message": json.dumps("Notification")})
    return HttpResponse("Done")


@login_required
def generatePoster(request):
    common_services_poster = CommonServicesPoster.objects.all()
    festivel_poster = FestivelPoster.objects.all()
    professional_poster = ProfessionalPoster.objects.all()
    branding_image = BrandingImage.objects.filter(user=request.user).last()
    context = {
        "is_poster": True,
        "common_services_poster": common_services_poster,
        "festivel_poster": festivel_poster,
        "professional_poster": professional_poster,
        "branding_image": branding_image,
        "room_name": "broadcast",
    }
    return render(request, "web/generate-poster.html", context)


@csrf_exempt
@login_required
def search_items(request):
    if request.POST:
        search_Key = request.POST["search_Key"]
        services = Services.objects.select_related("service_head").filter(Q(service_head__title__icontains=search_Key) | Q(title__icontains=search_Key))
        new_service_poster = NewServicePoster.objects.filter(Q(title__icontains=search_Key))
        important_poster = ImportantPoster.objects.filter(Q(title__icontains=search_Key))
        common_services_poster = CommonServicesPoster.objects.filter(Q(title__icontains=search_Key))
        festivel_poster = FestivelPoster.objects.filter(Q(title__icontains=search_Key))
        professional_poster = ProfessionalPoster.objects.filter(Q(title__icontains=search_Key))
        result = chain(services, new_service_poster, important_poster, common_services_poster, festivel_poster, professional_poster)
        print(services.count())
        context = {}
        context["template"] = render_to_string("web/service-searching.html", {"result": result}, request=request)
    return JsonResponse(context)


@login_required
def generateBill(request):
    services = Services.objects.all()
    context = {"is_bill": True, "services": services, "room_name": "broadcast"}
    return render(request, "web/generate-bill.html", context)


@csrf_exempt
@login_required
def searching_invoice(request):
    search = ''
    invoice = ''
    if 'search' in request.GET:
        search = request.GET['search']
        invoice = InvoiceItem.objects.filter(invoice__customer__phone_no__icontains=search)
    else:
        invoice = InvoiceItem.objects.all()
    context = {"is_search": True, 'invoice': invoice, }
    return render(request, 'web/invoice-searching.html', context)
    return JsonResponse(context)


@login_required
def generateForms(request):
    generate_forms = DownloadForms.objects.all()
    context = {"is_form": True, "generate_forms": generate_forms, "room_name": "broadcast"}
    return render(request, "web/generate-form.html", context)


@login_required
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response["Content-Disposition"] = "inline;filename=" + os.path.basename(file_path)
            return response
    raise Http404


@login_required
def documents(request):
    documents = DownloadDocuments.objects.all()
    context = {"is_document": True, "documents": documents, "room_name": "broadcast"}
    return render(request, "web/documents.html", context)


@login_required
def software(request):
    softwares = Softwares.objects.all()
    context = {"is_software": True, "softwares": softwares, "room_name": "broadcast"}
    return render(request, "web/softwares.html", context)


@login_required
def tools(request):
    tools = Tools.objects.all()
    context = {"is_tool": True, "tools": tools, "room_name": "broadcast"}
    return render(request, "web/tools.html", context)


@login_required
def marketingTip(request):
    marketing_tips = MarketingTips.objects.all()
    context = {"is_tip": True, "marketing_tips": marketing_tips, "room_name": "broadcast"}

    return render(request, "web/marketing-tip.html", context)


@login_required
def otherIdea(request):
    other_ideas = OtherIdeas.objects.all()
    context = {"is_idea": True, "other_ideas": other_ideas, "room_name": "broadcast"}
    return render(request, "web/other-ideas.html", context)


@login_required
def agencyPortal(request):
    agency_portal = AgencyPortal.objects.all()
    context = {"is_portal": True, "agency_portal": agency_portal, "room_name": "broadcast"}
    return render(request, "web/agency-portal.html", context)


@login_required
def backOfficeServices(request):
    back_office_services = BackOfficeServices.objects.all()
    context = {"is_backservice": True, "back_office_services": back_office_services, "room_name": "broadcast"}
    return render(request, "web/back-office-services.html", context)


@login_required
def bonus(request):
    agent_bonus = AgentBonus.objects.all()
    context = {"is_bonus": True, "agent_bonus": agent_bonus, "room_name": "broadcast"}
    return render(request, "web/bonus.html", context)


@login_required
def support(request):
    user = request.user
    upgraded = ""
    subscription = Subscription.objects.filter(user=user, is_active=True)
    for subs in subscription:
        upgraded = subs.is_active

    context = {"is_support": True, "upgraded": upgraded , "room_name": "broadcast"}
    return render(request, "web/support.html", context)


@login_required
def supportRequest(request):
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
def F_A_Q(request):
    Frequently_Asked_Questions = FAQ.objects.all()
    context = {"Frequently_Asked_Questions": Frequently_Asked_Questions, "room_name": "broadcast"}
    return render(request, "web/faq.html", context)


@login_required
def supportTicket(request):
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
def call_support(request):
    call_support = CallSupport.objects.all()
    context = {"call_support": call_support}
    return render(request, "web/call-support.html", context)


@login_required
def whatsapp_support(request):
    whatsapp_support = WhatsappSupport.objects.all()
    context = {"whatsapp_support": whatsapp_support}
    return render(request, "web/whatsapp-support.html", context)


def termsConditions(request):
    context = {}
    return render(request, "web/terms&conditions.html", context)


def payment(request):
    context = {}
    return render(request, "web/payment.html", context)


def paymentsuccess(request):
    context = {}
    return render(request, "web/paymentsuccess.html", context)


def paymentfail(request):
    context = {}
    return render(request, "web/paymentfail.html", context)


@login_required
def certificate_view(request):
    context = {"logined_user": request.user}
    return render(request, "web/certificate.html", context)


def upgrade_plan_request(request):
    context = {}
    return render(request, 'web/upgrade-request.html', context)


def buy_now_branding_image(request):
    context = {}
    return render(request, 'web/buy-now.html', context)
