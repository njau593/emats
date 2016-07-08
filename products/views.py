from django.shortcuts import render
from .models import detailedService, service

# Create your views here.

def products(request):
    product=service.objects.all()
    det_product=detailedService.objects.all()
    return render(request, 'pages/products.html', {'product':product})
