from django.shortcuts import render
from .models import aboutUs, Images, Reviews, Proverbs
from django.utils import timezone
from products.models import detailedService

# Create your views here.

def home(request):
    photos=Images.objects.all()
    misemo=Proverbs.objects.order_by('-Proverb_creation_date')
    custReview=Reviews.objects.all()
    offer = detailedService.objects.order_by('-service_CreateDate').all()[:3]

    return render(request, 'pages/home.html', {
        'photos':photos, 'offer':offer,
        'misemo':misemo, 'custReview':custReview
    })

def about(request):
    us=aboutUs.objects.all()
    return render(request, 'pages/about.html', {'us':us})
