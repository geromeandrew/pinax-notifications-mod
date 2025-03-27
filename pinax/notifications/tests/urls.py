from django.urls import include, re_path as url

urlpatterns = [
    url(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
]
