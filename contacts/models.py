from django.db import models
from django.utils.translation import ugettext_lazy as _

#Imported from django newsletter subscription package
from newsletter_subscription.models import SubscriptionBase

# Create your models here.

#Model for contacts
class reachUs(models.Model):
    Contact_name=models.CharField(max_length=50, null=True)
    Contact_number=models.BigIntegerField(null=True)
    Contact_address=models.TextField(null=True)
    Contact_email_address=models.TextField(null=True)
    Contact_location=models.TextField(null=True, blank=True)

#Model for newsletter
'''class newsletter(SubscriptionBase):
    Name = models.CharField(_('Name'), max_length=100, blank=True)'''

'''Name=models.CharField(max_length=100, null=True, blank=True)
Email=models.CharField(max_length=200)'''
