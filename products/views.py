from django.shortcuts import render
from .models import detailedService, service

# Create your views here.

def products(request):
    product=service.objects.all()
    det_product=detailedService.objects.order_by('serviceTitle')
    return render(request, 'pages/products.html', {
    'product':product, 'det_product':det_product
    })
