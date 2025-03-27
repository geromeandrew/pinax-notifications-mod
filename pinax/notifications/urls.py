from django.urls import re_path as url

from .views import NoticeSettingsView

app_name = "pinax_notifications"

urlpatterns = [
    url(r"^settings/$", NoticeSettingsView.as_view(), name="notice_settings"),
]
