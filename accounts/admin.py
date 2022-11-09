from django.contrib import admin
from .models import User
from django.contrib.auth.forms import UserChangeForm
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext as _


# Register your models here.
class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User




class MyUserAdmin(ImportExportModelAdmin):
    form = MyUserChangeForm
    list_display = (
        "email",
        "phone",
        "id",
        "shop_name",
        "district",
        "pincode",
        "category",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    autocomplete_fields = ("groups",)
    readonly_fields = ("last_login", "date_joined")
    search_fields = ("email", "shop_name")
    ordering = ("email",)
    exclude = ()
    # fieldsets = (
    #     (_("Authentication"), {"fields": ("phone", "password")}),
    #     (_("Personal info"), {"fields": ("shop_name","shop_address")}),
    #     (
    #         _("Permissions"),
    #         {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
    #     ),
    #     (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    #     (
    #         _("User Info"),
    #         {
    #             "fields": (
    #                 "email",
    #                 "phone",
    #                 "id",
    #                 "shop_name",
    #                 "shop_address",
    #                 "district",
    #                 "pincode",
    #                 "profile_image",
    #                 "category",
    #                 "is_user",
    #             )
    #         },
    #     ),
    # )
admin.site.register(User, MyUserAdmin)
