from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from .admin_content_lang import get_content_lang
from .admin_forms import CertificateForm, InterestForm, ResumeProfileForm
from .admin_mixins import ContentLanguageAdminMixin
from .admin_site import cv_admin_site
from .models import Certificate, Interest, ResumeProfile, SiteSettings

cv_admin_site.register(User, UserAdmin)
cv_admin_site.register(Group, GroupAdmin)


@admin.register(SiteSettings, site=cv_admin_site)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("theme",)

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ResumeProfile, site=cv_admin_site)
class ResumeProfileAdmin(ContentLanguageAdminMixin, admin.ModelAdmin):
    form = ResumeProfileForm
    fieldsets = (
        (
            _("Resume text"),
            {
                "description": _("Edit one language at a time. Use the language strip above, then Save."),
                "fields": ("full_name", "headline", "about", "location"),
            },
        ),
        (_("Photo & contacts"), {"fields": ("photo", "email", "phone", "website", "linkedin", "github")}),
    )

    def has_add_permission(self, request):
        return not ResumeProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Certificate, site=cv_admin_site)
class CertificateAdmin(ContentLanguageAdminMixin, admin.ModelAdmin):
    form = CertificateForm
    list_display = ("title_display", "issued_on", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "pk")

    @admin.display(description=_("Title"))
    def title_display(self, obj):
        lang = get_content_lang(getattr(self, "request", None))
        return getattr(obj, f"title_{lang}", "") or obj.title_en

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)

    fieldsets = (
        (
            _("Certificate text"),
            {"fields": ("title", "issuer", "description")},
        ),
        (_("Files & order"), {"fields": ("image", "document", "issued_on", "sort_order")}),
    )


@admin.register(Interest, site=cv_admin_site)
class InterestAdmin(ContentLanguageAdminMixin, admin.ModelAdmin):
    form = InterestForm
    list_display = ("label_display", "sort_order")
    list_editable = ("sort_order",)
    ordering = ("sort_order", "pk")

    @admin.display(description=_("Interest"))
    def label_display(self, obj):
        lang = get_content_lang(getattr(self, "request", None))
        return getattr(obj, f"label_{lang}", "") or obj.label_en

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)

    fieldsets = (
        (_("Interest text"), {"fields": ("label", "detail")}),
        (_("Order"), {"fields": ("sort_order",)}),
    )
