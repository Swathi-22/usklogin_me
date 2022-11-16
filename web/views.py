import json
import os
import uuid
from itertools import chain
from accounts.models import User
from services.models import BrandingImage
from services.models import ServiceHeads
from services.models import Services
from web.models import FAQ
from web.models import AgencyPortal
from web.models import AgentBonus
from web.models import BackOfficeServices
from web.models import CallSupport
from web.models import CertificateImages
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
from web.models import Tools
from web.models import WhatsappSupport
from invoices.models import Invoice
import razorpay
from .forms import SupportRequestForm
from .forms import SupportTicketForm
from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .functions import generate_pw
from .helper import send_forget_password_mail
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.views.decorators.csrf import csrf_exempt



RAZOR_PAY_KEY = "rzp_test_kVa6uUqaP96eJr"
RAZOR_PAY_SECRET = "SMxZvHU0XyiAIwMoLIqFL7Na"


def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    temp_pass = generate_pw()
    print(temp_pass)
    context = {"user_form": user_form}
    if request.method == "POST":
        if user_form.is_valid():
            data = user_form.save(commit=False)
            data.username = request.POST.get("phone")
            data.temp_password = temp_pass
            data.set_password(temp_pass)
            data.save()
            messages.success(request, "You have successfully registered!")
            return redirect("web:order_payment", pk=data.pk)
    return render(request, "web/register.html", context)


def order_payment(request, pk):
    user = User.objects.get(id=pk)
    amount = 20000
    client = razorpay.Client(auth=(RAZOR_PAY_KEY, RAZOR_PAY_SECRET))
    razorpay_order = client.order.create({"amount": amount, "currency": "INR", "payment_capture": "1"})
    order, created = Order.objects.get_or_create(user=user, amount=amount, provider_order_id=razorpay_order["id"])
    context = {"order": order, "amount": amount, "razorpay_key": RAZOR_PAY_KEY, "razorpay_order": razorpay_order, "callback_url": "http://" + "127.0.0.1:8000" + "/callback/"}
    return render(request, "web/payment.html", context)


def verify_signature(response_data):
    client = razorpay.Client(auth=(RAZOR_PAY_KEY, RAZOR_PAY_SECRET))
    return client.utility.verify_payment_signature(response_data)


@csrf_exempt
def callback(request):
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        response_data = {"razorpay_order_id": provider_order_id, "razorpay_payment_id": payment_id, "razorpay_signature": signature_id}

        if verify_signature(response_data):
            order = Order.objects.get(provider_order_id=provider_order_id)
            order_status = PaymentStatus.SUCCESS
            order.status = PaymentStatus.SUCCESS
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
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
            send_mail(subject,message, "secure.gedexo@gmail.com", [email], fail_silently=False)
            messages.success(request, "Payment Successful")
        else:
            order_status = PaymentStatus.FAILURE
        return render(request, "web/callback.html", context={"status": order_status})
    else:
        return render(request, "web/payment.html")


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


@login_required
def profile(request):
    user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
    context = {"is_profile": True, "user_form": user_form}
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


def settings(request):
    context = {}
    return render(request, "web/settings.html", context)


def index(request):
    service_head = ServiceHeads.objects.all()
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all()
    important_poster = ImportantPoster.objects.all()
    branding_image = BrandingImage.objects.all()
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


def generatePoster(request):
    common_services_poster = CommonServicesPoster.objects.all()
    festivel_poster = FestivelPoster.objects.all()
    professional_poster = ProfessionalPoster.objects.all()
    branding_image = BrandingImage.objects.all()
    context = {
        "is_poster": True,
        "common_services_poster": common_services_poster,
        "festivel_poster": festivel_poster,
        "professional_poster": professional_poster,
        "branding_image": branding_image,
        "room_name": "broadcast",
    }
    return render(request, "web/generate-poster.html", context)



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


def generateBill(request):
    services = Services.objects.all()
    context = {"is_bill": True, "services": services, "room_name": "broadcast"}
    return render(request, "web/generate-bill.html", context)


def search_invoice(request):
   if request.POST:
    invoice_search_key = request.POST["search_invoice"]
    invoice_list = Invoice.objects.select_related("customer").filter(Q(customer__phone_no__icontains=invoice_search_key))



@login_required
def generateForms(request):
    generate_forms = DownloadForms.objects.all()
    context = {"is_form": True, "generate_forms": generate_forms, "room_name": "broadcast"}
    return render(request, "web/generate-form.html", context)


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


def marketingTip(request):
    marketing_tips = MarketingTips.objects.all()
    context = {"is_tip": True, "marketing_tips": marketing_tips, "room_name": "broadcast"}
    return render(request, "web/marketing-tip.html", context)


def otherIdea(request):
    other_ideas = OtherIdeas.objects.all()
    context = {"is_idea": True, "other_ideas": other_ideas, "room_name": "broadcast"}
    return render(request, "web/other-ideas.html", context)


def agencyPortal(request):
    agency_portal = AgencyPortal.objects.all()
    context = {"is_portal": True, "agency_portal": agency_portal, "room_name": "broadcast"}
    return render(request, "web/agency-portal.html", context)


def backOfficeServices(request):
    back_office_services = BackOfficeServices.objects.all()
    context = {"is_backservice": True, "back_office_services": back_office_services, "room_name": "broadcast"}
    return render(request, "web/back-office-services.html", context)


def bonus(request):
    agent_bonus = AgentBonus.objects.all()
    context = {"is_bonus": True, "agent_bonus": agent_bonus, "room_name": "broadcast"}
    return render(request, "web/bonus.html", context)


def support(request):
    context = {"is_support": True, "room_name": "broadcast"}
    return render(request, "web/support.html", context)


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


def F_A_Q(request):
    Frequently_Asked_Questions = FAQ.objects.all()
    context = {"Frequently_Asked_Questions": Frequently_Asked_Questions, "room_name": "broadcast"}
    return render(request, "web/faq.html", context)


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


def call_support(request):
    call_support = CallSupport.objects.all()
    phone = request.session["phone"]
    user = User.objects.filter(phone=phone).first()
    order = Order.objects.get(name=user)
    if order.amount == 20000:
        return redirect("web:upgrade_plan")
    context = {"call_support": call_support}
    return render(request, "web/call-support.html", context)


# def upgrade_plan(request):
#     phone = request.session["phone"]
#     amount = 50000
#     client = razorpay.Client(auth=("rzp_test_kVa6uUqaP96eJr", "SMxZvHU0XyiAIwMoLIqFL7Na"))
#     razorpay_order = client.order.create({"amount": amount, "currency": "INR", "payment_capture": "1"})
#     obj = User.objects.filter(phone=phone).first()
#     order = Order.objects.create(name=obj, amount=amount, provider_order_id=razorpay_order["id"])
#     order.save()
#     return render(request,"web/upgrade-plan.html",{
#                 # "callback_url": "https://" + "usklogin.geany.website" + "/callback/",
#                 "callback_url": "http://" + "127.0.0.1:8000" + "/callback/",
#                 "razorpay_key": "rzp_test_kVa6uUqaP96eJr",
#                 "order": order,},)


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


def certificate_view(request):
    context = {"logined_user": request.user, "room_name": "broadcast"}
    return render(request, "web/certificate.html", context)


def pdf_certificate(request):
    certificate_images = CertificateImages.objects.all()
    template_path = "web/certificate-pdf.html"
    context = {"certificate_images": certificate_images}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="usklogin-certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


def logout_view(request):
    try:
        del request.session["phone"]
    except:
        return redirect("web:login_view")
    return redirect("web:login_view")
