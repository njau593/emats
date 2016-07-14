from django.db import models
from django.utils import timezone

# Create your models here.

#Models for home
class Images(models.Model):
    picture=models.ImageField(null=True, blank=True)

class Proverbs(models.Model):
    Proverb_creation_date=models.DateField(default=timezone.now)
    Proverb_publish_date=models.DateField(null=False, blank=False)
    Proverb=models.TextField(null=False)
    Proverb_translation=models.TextField(null=True, blank=True)
    Proverb_meaning=models.TextField(null=False, blank=False)

class Reviews(models.Model):
    Review_title=models.TextField(null=False)
    Review_customer_name=models.CharField(null=True, blank=True, max_length=100)
    Review_narration=models.TextField(null=False)
    Review_image=models.ImageField(null=True, blank=True)

#Models for about
class aboutUs(models.Model):
    title=models.CharField(max_length=50)
    post=models.TextField(null=False)

#Models for contacts
class reachUs(models.Model):
    Contact_name=models.CharField(max_length=50, null=True)
    Contact_number=models.IntegerField(null=True)
    Contact_address=models.TextField(null=True)
    Contact_email_address=models.TextField(null=True)
    Contact_location=models.TextField(null=True, blank=True)

'''class keProfile(models.Model):
    prof_title= models.CharField(max_length=100)
    prof_text= models.TextField()

    def prof_publish(self):
        self.save()

    def __str__(self):
        return self.prof_title

class postInfo(models.Model):
    post_author= models.ForeignKey('auth.User')
    post_title= models.CharField(max_length=200)
    post_text= models.TextField()
    post_create_date= models.DateTimeField(default=timezone.now)
    post_pub_date= models.DateTimeField(blank=True, null=True)

    def post_publish(self):
        self.post_pub_date=timezone.now()
        self.save()

    def __str__(self):
        return self.post_title

class aboutUs(models.Model):
    title=models.CharField(max_length=50)
    post=models.TextField(null=False)

class reachUs(models.Model):
    con_name=models.CharField(max_length=50, null=True)
    cont_number=models.IntegerField(null=True)
    cont_address=models.TextField(null=True)
    cont_email_address=models.TextField(null=True)
    cont_location=models.TextField(default="Mombasa")
'''
