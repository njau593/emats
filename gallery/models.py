from django.db import models
from django.utils import timezone

# Create your models here.

class pictures(models.Model):
    Photo=models.ImageField(null=True, blank=True, upload_to='gallery')
    Photo_date=models.DateField(blank=True)
    Photo_caption=models.TextField(null=False)
