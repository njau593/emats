from django.shortcuts import render
from .models import aboutUs, Images, Reviews, Proverbs
from django.utils import timezone

# Create your views here.

def home(request):
    photos=Images.objects.all()
    misemo=Proverbs.objects.order_by('-Proverb_creation_date')
    custReview=Reviews.objects.all()
    return render(request, 'pages/home.html', {
        'photos':photos,
        'misemo':misemo, 'custReview':custReview
    })

def about(request):
    us=aboutUs.objects.all()
    return render(request, 'pages/about.html', {'us':us})
