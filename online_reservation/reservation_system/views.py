from django.forms import forms, fields
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Reservation, Service, Category, Company
from django.views import generic
from formset import widgets, calendar, views
from formset.utils import FormMixin
from formset.renderers.tailwind import FormRenderer


# Create your views here.
class ServiceView(generic.ListView):
    template_name = "reservation_system/service.html"
    context_object_name = "service_list"
    def get_queryset(self):
        # name = self.request.GET.get('name', '')
        # print(name)
        # print("HALO")
        # object_list = Service.objects.all()
        # if name:
        #     object_list = object_list.filter(name__icontains=name)
        # return object_list
        company_id = self.kwargs['pk']
        company = get_object_or_404(Company, pk=company_id)
        return Service.objects.filter(company=company)
    
class CompanyView(generic.ListView):
    template_name = "reservation_system/company.html"
    context_object_name = "company_list"
    def get_queryset(self):
        category_id = self.kwargs['pk']
        category = get_object_or_404(Category, pk=category_id)
        print(category_id)
        print(category) 
        return Company.objects.filter(categories=category)

class CategoryView(generic.ListView):
    template_name = "reservation_system/category.html"
    context_object_name = "category_list"
    def get_queryset(self):
        return Category.objects.all()
 
# Reservation view
class AppointmentForm(FormMixin, forms.Form):
    # default_renderer = FormRenderer()
    auguration_date = fields.DateField(widget=widgets.DateCalendar(attrs={'click': 'submit -> proceed'}))

def my_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        print('is valid', form.is_valid(), request.POST.get('formset_data'))
        if form.is_valid():
            # Handle form data here
            return HttpResponse('test')
    else:
        form = AppointmentForm()
    return render(request, "reservation_system/reservation.html", {'form': form})