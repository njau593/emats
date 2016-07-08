from django.db import models

# Create your models here.

class kenyaInfo(models.Model):
    keTitle=models.CharField(max_length=20)
    keInfo=models.TextField()
    keImage=models.ImageField(null=True)
