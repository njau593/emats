from django.db import models

# Create your models here.

class kenyaInfo(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    Image=models.ImageField(null=True, blank=True)
