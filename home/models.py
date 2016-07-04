from django.db import models
from django.utils import timezone

# Create your models here.

class keProfile(models.Model):
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
    cont_location=models.TextField(default="Mombasa")

class service(models.Model):
    pro_title=models.CharField(max_length=50)
    pro_descriiption=models.TextField()
