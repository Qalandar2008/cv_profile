from django.urls import path

from . import dashboard_views as v

app_name = "dashboard"

urlpatterns = [
    path("login/", v.DashboardLoginView.as_view(), name="login"),
    path("logout/", v.DashboardLogoutView.as_view(), name="logout"),
    path("", v.dashboard_index, name="index"),
    path("profile/", v.dashboard_profile, name="profile"),
    path("certificates/", v.certificate_list, name="certificates"),
    path("certificates/new/", v.certificate_create, name="certificate_create"),
    path("certificates/<int:pk>/edit/", v.certificate_edit, name="certificate_edit"),
    path("certificates/<int:pk>/delete/", v.certificate_delete, name="certificate_delete"),
    path("interests/", v.interest_list, name="interests"),
    path("interests/new/", v.interest_create, name="interest_create"),
    path("interests/<int:pk>/edit/", v.interest_edit, name="interest_edit"),
    path("interests/<int:pk>/delete/", v.interest_delete, name="interest_delete"),
    path("settings/", v.dashboard_settings, name="settings"),
    path("samples/list/", v.sample_list_page, name="samples_list"),
    path("samples/form/", v.sample_form_page, name="samples_form"),
]
