from .models import Note
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin, ImportExportModelAdmin):
    form = MyUserChangeForm
    list_display = ("id", "email", "phone", "shop_name", "district", "pincode", "category")
    list_filter = ("is_active", "is_staff", "is_superuser")
    autocomplete_fields = ("groups",)
    readonly_fields = ("last_login", "date_joined")
    search_fields = ("email", "shop_name")
    ordering = ("email",)
    fieldsets = (
        (_("Authentication"), {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "name", "phone", "shop_name", "shop_address", "district", "pincode", "category", "profile_image")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(User, MyUserAdmin)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "note", "created_by", "created")
    list_filter = ("created_by",)
    search_fields = ("title", "note")
    ordering = ("title",)
    fieldsets = ((_("Note"), {"fields": ("title", "note", "created_by")}),)
