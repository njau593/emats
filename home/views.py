from django.shortcuts import render
from .models import aboutUs, postInfo, keProfile
from .models import reachUs
from django.utils import timezone

# Create your views here.

def home(request):
    profile=keProfile.objects.all()
    info=postInfo.objects.all()
    return render(request, 'pages/home.html', {'profile':profile, 'info':info})

def about(request):
    us=aboutUs.objects.all()
    return render(request, 'pages/about.html', {'us':us})

def contacts(request):
    card=reachUs.objects.all()
    return render(request, 'pages/contacts.html', {'card':card})
