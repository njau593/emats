from django.shortcuts import render
from .models import aboutUs, Images, Reviews, Proverbs
from django.utils import timezone

# Create your views here.

def home(request):
    photos1=Images.objects.get(pk=1)
    photos2=Images.objects.get(pk=2)
    photos3=Images.objects.get(pk=3)
    misemo=Proverbs.objects.order_by('-Proverb_creation_date')
    custReview=Reviews.objects.all()
    return render(request, 'pages/home.html', {
        'photos1':photos1, 'photos2':photos2, 'photos3':photos3,
        'misemo':misemo, 'custReview':custReview
    })

def about(request):
    us=aboutUs.objects.all()
    return render(request, 'pages/about.html', {'us':us})

'''def contacts(request):
    card=reachUs.objects.all()
    return render(request, 'pages/contacts.html', {'card':card})'''
