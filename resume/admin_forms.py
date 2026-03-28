from django import forms
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from .admin_content_lang import content_lang_label, get_content_lang
from .models import Certificate, Interest, ResumeProfile


class _RequestModelForm(forms.ModelForm):
    """request orqali kontent tilini aniqlaydi."""

    def __init__(self, *args, request=None, **kwargs):
        self.request = request
        self._content_lang = get_content_lang(request)
        super().__init__(*args, **kwargs)


def _suffix_label(base_lazy, lang: str) -> str:
    return f"{force_str(base_lazy)} ({content_lang_label(lang)})"


class ResumeProfileForm(_RequestModelForm):
    full_name = forms.CharField(max_length=200, required=False)
    headline = forms.CharField(max_length=300, required=False)
    about = forms.CharField(widget=forms.Textarea(attrs={"rows": 6}), required=False)
    location = forms.CharField(max_length=200, required=False)

    class Meta:
        model = ResumeProfile
        fields = (
            "photo",
            "email",
            "phone",
            "website",
            "linkedin",
            "github",
        )

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, request=request, **kwargs)
        L = self._content_lang
        self.fields["full_name"].label = _suffix_label(_("Full name"), L)
        self.fields["headline"].label = _suffix_label(_("Headline / role"), L)
        self.fields["about"].label = _suffix_label(_("About"), L)
        self.fields["location"].label = _suffix_label(_("Location"), L)

        inst = self.instance
        if inst and getattr(inst, "pk", None):
            self.fields["full_name"].initial = getattr(inst, f"full_name_{L}", "") or ""
            self.fields["headline"].initial = getattr(inst, f"headline_{L}", "") or ""
            self.fields["about"].initial = getattr(inst, f"about_{L}", "") or ""
            self.fields["location"].initial = getattr(inst, f"location_{L}", "") or ""

    def save(self, commit=True):
        inst = self.instance
        L = self._content_lang
        stored = {}
        for base in ("full_name", "headline", "about", "location"):
            for s in ("en", "uz", "ru"):
                key = f"{base}_{s}"
                stored[key] = getattr(inst, key, "") or ""

        obj = super().save(commit=False)

        for base in ("full_name", "headline", "about", "location"):
            for s in ("en", "uz", "ru"):
                setattr(obj, f"{base}_{s}", stored[f"{base}_{s}"])

        setattr(obj, f"full_name_{L}", self.cleaned_data.get("full_name", "") or "")
        setattr(obj, f"headline_{L}", self.cleaned_data.get("headline", "") or "")
        setattr(obj, f"about_{L}", self.cleaned_data.get("about", "") or "")
        setattr(obj, f"location_{L}", self.cleaned_data.get("location", "") or "")

        if commit:
            obj.save()
        return obj


class CertificateForm(_RequestModelForm):
    title = forms.CharField(max_length=300, required=False)
    issuer = forms.CharField(max_length=200, required=False)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}), required=False)

    class Meta:
        model = Certificate
        fields = ("image", "document", "issued_on", "sort_order")

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, request=request, **kwargs)
        L = self._content_lang
        self.fields["title"].label = _suffix_label(_("Title"), L)
        self.fields["issuer"].label = _suffix_label(_("Issuer / organization"), L)
        self.fields["description"].label = _suffix_label(_("Description"), L)

        inst = self.instance
        if inst and getattr(inst, "pk", None):
            self.fields["title"].initial = getattr(inst, f"title_{L}", "") or ""
            self.fields["issuer"].initial = getattr(inst, f"issuer_{L}", "") or ""
            self.fields["description"].initial = getattr(inst, f"description_{L}", "") or ""

    def save(self, commit=True):
        inst = self.instance
        L = self._content_lang
        stored = {}
        for base in ("title", "issuer", "description"):
            for s in ("en", "uz", "ru"):
                key = f"{base}_{s}"
                stored[key] = getattr(inst, key, "") or ""

        obj = super().save(commit=False)

        for base in ("title", "issuer", "description"):
            for s in ("en", "uz", "ru"):
                setattr(obj, f"{base}_{s}", stored[f"{base}_{s}"])

        setattr(obj, f"title_{L}", self.cleaned_data.get("title", "") or "")
        setattr(obj, f"issuer_{L}", self.cleaned_data.get("issuer", "") or "")
        setattr(obj, f"description_{L}", self.cleaned_data.get("description", "") or "")

        if commit:
            obj.save()
        return obj


class InterestForm(_RequestModelForm):
    label = forms.CharField(max_length=200, required=False)
    detail = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}), required=False)

    class Meta:
        model = Interest
        fields = ("sort_order",)

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, request=request, **kwargs)
        L = self._content_lang
        self.fields["label"].label = _suffix_label(_("Interest"), L)
        self.fields["detail"].label = _suffix_label(_("Details"), L)

        inst = self.instance
        if inst and getattr(inst, "pk", None):
            self.fields["label"].initial = getattr(inst, f"label_{L}", "") or ""
            self.fields["detail"].initial = getattr(inst, f"detail_{L}", "") or ""

    def save(self, commit=True):
        inst = self.instance
        L = self._content_lang
        stored = {}
        for base in ("label", "detail"):
            for s in ("en", "uz", "ru"):
                key = f"{base}_{s}"
                stored[key] = getattr(inst, key, "") or ""

        obj = super().save(commit=False)

        for base in ("label", "detail"):
            for s in ("en", "uz", "ru"):
                setattr(obj, f"{base}_{s}", stored[f"{base}_{s}"])

        setattr(obj, f"label_{L}", self.cleaned_data.get("label", "") or "")
        setattr(obj, f"detail_{L}", self.cleaned_data.get("detail", "") or "")

        if commit:
            obj.save()
        return obj
