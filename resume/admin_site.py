from django.contrib.admin import AdminSite

from .ui_strings import ui_text


class CVAdminSite(AdminSite):
    """Grand vine palitrasi alohida CSS orqali; sarlavhalar ui_text orqali 3 tilda."""

    site_url = "/"

    def each_context(self, request):
        ctx = super().each_context(request)
        ctx["site_header"] = ui_text("admin_title")
        ctx["site_title"] = ui_text("admin_site")
        return ctx

    def index(self, request, extra_context=None):
        old_title = self.index_title
        self.index_title = ui_text("admin_dashboard")
        try:
            return super().index(request, extra_context)
        finally:
            self.index_title = old_title


cv_admin_site = CVAdminSite(name="admin")
