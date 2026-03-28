from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from .admin_site import cv_admin_site

cv_admin_site.register(User, UserAdmin)
cv_admin_site.register(Group, GroupAdmin)
from .models import Certificate, Interest, ResumeProfile, SiteSettings


@admin.register(SiteSettings, site=cv_admin_site)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("theme",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ResumeProfile, site=cv_admin_site)
class ResumeProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("Photo & contacts"), {"fields": ("photo", "email", "phone", "website", "linkedin", "github")}),
        (_("English"), {"fields": ("full_name_en", "headline_en", "about_en", "location_en")}),
        (_("Uzbek"), {"fields": ("full_name_uz", "headline_uz", "about_uz", "location_uz")}),
        (_("Russian"), {"fields": ("full_name_ru", "headline_ru", "about_ru", "location_ru")}),
    )

    def has_add_permission(self, request):
        return not ResumeProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Certificate, site=cv_admin_site)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title_en", "issued_on", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "pk")
    fieldsets = (
        (_("English"), {"fields": ("title_en", "issuer_en", "description_en")}),
        (_("Uzbek"), {"fields": ("title_uz", "issuer_uz", "description_uz")}),
        (_("Russian"), {"fields": ("title_ru", "issuer_ru", "description_ru")}),
        (_("Files & meta"), {"fields": ("image", "document", "issued_on", "sort_order")}),
    )


@admin.register(Interest, site=cv_admin_site)
class InterestAdmin(admin.ModelAdmin):
    list_display = ("label_en", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "pk")
    fieldsets = (
        (_("English"), {"fields": ("label_en", "detail_en")}),
        (_("Uzbek"), {"fields": ("label_uz", "detail_uz")}),
        (_("Russian"), {"fields": ("label_ru", "detail_ru")}),
        (_("Order"), {"fields": ("sort_order",)}),
    )
