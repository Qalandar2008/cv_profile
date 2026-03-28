from django.conf import settings
from django.urls import translate_url

from .models import SiteSettings


def site_theme(request):
    return {"active_theme": SiteSettings.load().theme}


def language_switch_urls(request):
    paths = {}
    for code, _ in settings.LANGUAGES:
        try:
            paths[code] = translate_url(request.path, code)
        except Exception:
            paths[code] = request.path
    return {"switch_urls": paths}
