from django.contrib import admin
from .models import Company, Reservation, Service, Customer, Category
# Register your models here.
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Reservation)
admin.site.register(Customer)
admin.site.register(Category)
