from django.shortcuts import redirect

from .admin_content_lang import SESSION_KEY, get_content_lang


class ContentLanguageAdminMixin:
    """?content_lang= uz | en | ru orqali sessiyani yangilab, bitta input rejimini yoqadi."""

    change_form_template = "admin/resume/cv_change_form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = getattr(self, "request", None)
        return kwargs

    def _redirect_strip_content_lang(self, request):
        cl = request.GET.get("content_lang")
        if cl in ("en", "uz", "ru") and request.method == "GET":
            request.session[SESSION_KEY] = cl
            q = request.GET.copy()
            del q["content_lang"]
            url = request.path
            if q:
                url = f"{url}?{q.urlencode()}"
            return redirect(url)
        return None

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        redir = self._redirect_strip_content_lang(request)
        if redir:
            return redir
        extra_context = extra_context or {}
        extra_context["admin_content_lang"] = get_content_lang(request)
        return super().changeform_view(request, object_id, form_url, extra_context)

    def add_view(self, request, form_url="", extra_context=None):
        redir = self._redirect_strip_content_lang(request)
        if redir:
            return redir
        extra_context = extra_context or {}
        extra_context["admin_content_lang"] = get_content_lang(request)
        return super().add_view(request, form_url, extra_context)
