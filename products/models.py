from django.db import models
from django.utils import timezone

# Create your models here.

class service(models.Model):
    product_Title=models.CharField(max_length=50)
    product_Description=models.TextField()
    product_Image=models.ImageField(null=True, blank=True, upload_to='products/images')

class detailedService(models.Model):
    service_Type=models.ForeignKey(service, on_delete=models.CASCADE, default=None)
    service_Title=models.CharField(max_length=50)
    service_Description=models.TextField()
    service_Image=models.ImageField(null=True, blank=True, upload_to='products/images')
    service_CreateDate=models.DateTimeField(default=timezone.now)
    service_ToBeDate=models.DateTimeField(blank=False, null=False, default=timezone.now)
    service_Location=models.TextField()
