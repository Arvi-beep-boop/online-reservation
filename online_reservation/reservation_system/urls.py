from django.urls import path

from . import views

app_name = "reservation_system"
urlpatterns = [
    path("", views.ServiceView.as_view(), name="service"),
]
