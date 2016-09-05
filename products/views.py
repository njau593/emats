from django.shortcuts import render
from .models import detailedService, service
from django.shortcuts import render, get_object_or_404

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
