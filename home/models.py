from django.db import models
from django.utils import timezone

# Create your models here.

#Models for home
class Images(models.Model):
    Picture=models.ImageField(null=True,upload_to='home')
    Picture_caption= models.TextField(null=True, blank=True)

class Proverbs(models.Model):
    Proverb_creation_date=models.DateField(default=timezone.now)
    Proverb_publish_date=models.DateField(null=False, blank=False)
    Proverb=models.TextField(null=False)
    Proverb_translation=models.TextField(null=True, blank=True)
    Proverb_meaning=models.TextField(null=False, blank=False)

class Reviews(models.Model):
    Review_title=models.CharField(null=False, max_length=50)
    Review_customer_name=models.CharField(null=True, blank=True, max_length=100)
    Review_narration=models.TextField(null=False)
    Review_image=models.ImageField(null=True, blank=True)

#Models for about
class aboutUs(models.Model):
    title=models.CharField(max_length=50)
    post=models.TextField(null=False)
