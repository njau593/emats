from django.db import models
from django.utils import timezone

# Create your models here.

class service(models.Model):
    productTitle=models.CharField(max_length=50)
    productDescription=models.TextField()
    productImage=models.ImageField(null=True)

class detailedService(models.Model):
    serviceType=models.ForeignKey(service, on_delete=models.CASCADE, default=None)
    serviceTitle=models.CharField(max_length=50)
    serviceDescription=models.TextField()
    serviceImage=models.ImageField(null=True)
    serviceCreateDate=models.DateTimeField(default=timezone.now)
    serviceToBeDate=models.DateTimeField(blank=False, null=False, default=timezone.now)
    serviceLocation=models.TextField()

'''class service(models.Model):
    productTitle=models.CharField(max_length=50)
    productDescription=models.TextField()
    productImage=models.ImageField(null=True)

class detailedService(models.Model):
    serviceTitle=models.CharField(max_length=50)
    serviceDescription=models.TextField()
    serviceImage=models.ImageField(null=True)
    serviceCreateDate=models.DateTimeField(default=timezone.now)
    serviceToBeDate=models.DateTimeField(blank=False, null=False, default=timezone.now)
    serviceLocation=models.TextField()'''
