from django.urls import path

from . import views

app_name = "reservation_system"
urlpatterns = [
    path("<int:pk>/service", views.ServiceView.as_view(), name="service"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("<int:pk>/company/", views.CompanyView.as_view(), name="company"),
    path("reservation/", views.my_view, name="reservation"),
]
