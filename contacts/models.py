from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

#Model for contacts
class reachUs(models.Model):
    Contact_name=models.CharField(max_length=50, null=True)
    Contact_number=models.BigIntegerField(null=True)
    Contact_address=models.TextField(null=True)
    Contact_email_address=models.TextField(null=True)
    Contact_location=models.TextField(null=True, blank=True)

#Model for newsletter
