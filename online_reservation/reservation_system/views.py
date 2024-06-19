from django.shortcuts import render
from .models import Service
from django.views import generic

# Create your views here.
class ServiceView(generic.ListView):
    template_name = "reservation_system/service.html"
    context_object_name = "service_list"
    def get_queryset(self):
        return Service.objects.all()

