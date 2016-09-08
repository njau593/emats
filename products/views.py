from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import detailedService, service

# Create your views here.
def products(request):
    product=service.objects.all()
    return render(request, 'pages/products.html', {
    'product':product
    })

def product_detail(request, pk):
    prods=get_object_or_404(service, pk=pk)
    det_product = detailedService.objects.all()
    return render(request, 'pages/product_detail.html', {
    'prods':prods, 'det_product':det_product
    })

def actual_product(request, pk):
    events = get_object_or_404(detailedService, pk=pk)
    return render(request, 'pages/actual_product.html', {
    'events':events
    })
