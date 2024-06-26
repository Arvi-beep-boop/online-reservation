from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    class Meta:
        abstract = True

class ContactInfo(models.Model):
    # email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Company(Address, ContactInfo):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
        
    def __str__(self):
        return self.name
    
class Customer(ContactInfo):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    duration = models.DurationField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    date = models.DateTimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)