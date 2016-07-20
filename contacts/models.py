from django.db import models

# Create your models here.

#Model for contacts
class reachUs(models.Model):
    Contact_name=models.CharField(max_length=50, null=True)
    Contact_number=models.IntegerField(null=True)
    Contact_address=models.TextField(null=True)
    Contact_email_address=models.TextField(null=True)
    Contact_location=models.TextField(null=True, blank=True)

#Model for newsletter
class newsletter(models.Model):
    Name=models.CharField(max_length=100, null=True, blank=True)
    Email=models.CharField(max_length=200)
