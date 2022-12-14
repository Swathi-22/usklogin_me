from .models import FAQ
from .models import AddonServices
from .models import AgencyPortal
from .models import AgentBonus
from .models import BackOfficeServices
from .models import CallSupport
from .models import CommonServicesPoster
from .models import DownloadDocuments
from .models import DownloadForms
from .models import FestivelPoster
from .models import ImportantPoster
from .models import LatestNews
from .models import MarketingTips
from .models import NewServicePoster
from .models import OnloadPopup
from .models import Order
from .models import OtherIdeas
from .models import ProfessionalPoster
from .models import Softwares
from .models import Subscription
from .models import SupportRequest
from .models import SupportTicket
from .models import Tools
from .models import WhatsappSupport
from .models import AgencyPortalService
from .models import SeasonalService
from .models import UpdatesorInformation
from .models import PromotionalPoster
from .models import Others

from django.contrib import admin


@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ("news",)


@admin.register(NewServicePoster)
class NewServicePosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(ImportantPoster)
class ImportantPosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(CommonServicesPoster)
class CommonServicesPosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(FestivelPoster)
class FestivelPosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(ProfessionalPoster)
class ProfessionalPosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(AgencyPortalService)
class AgencyPortalServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(SeasonalService)
class SeasonalServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(UpdatesorInformation)
class UpdatesorInformationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(PromotionalPoster)
class PromotionalPosterAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(Others)
class OthersAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")


@admin.register(DownloadForms)
class generate_formsAdmin(admin.ModelAdmin):
    list_display = ("name", "file")


@admin.register(DownloadDocuments)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ("name", "file")


@admin.register(Softwares)
class SoftwaresAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(MarketingTips)
class MarketingTipsAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(OtherIdeas)
class OtherIdeasAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(AgencyPortal)
class AgencyPortalAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(BackOfficeServices)
class BackOfficeServicesAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(AgentBonus)
class AgentBonusAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "title")


@admin.register(SupportRequest)
class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ("ticket_id", "name", "email", "phone")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status")


@admin.register(CallSupport)
class CallSupportAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")


@admin.register(WhatsappSupport)
class WhatsappSupportAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number")


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status", "valid_from", "valid_upto")
    list_filter = ("status", "valid_from", "valid_upto")
    ordering = ["user"]


@admin.register(AddonServices)
class AddonServicesAdmin(admin.ModelAdmin):
    list_display = ("name", "link")


@admin.register(OnloadPopup)
class OnloadPopupAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
