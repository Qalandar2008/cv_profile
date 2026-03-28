from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from resume.admin_site import cv_admin_site

"""
Til: set_language (/i18n/setlang/) + cookie + CookieAwareLocaleMiddleware.
i18n_patterns olib tashlandi — / va /admin/ har doim topiladi (404 bo‘lmasin).
"""

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", cv_admin_site.urls),
    path("dashboard/", include("resume.dashboard_urls", namespace="dashboard")),
    path("", include("resume.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
