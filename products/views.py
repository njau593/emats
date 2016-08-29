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

    for i in service.id:
        if i == detailedService.service_Type_id:
            det_product = detailedService.objects.order_by('service_ToBeDate')

    return render(request, 'pages/product_detail.html', {
    'prods':prods, 'det_product':det_product
    })


'''det_product=detailedService.objects.all()
det_product2=detailedService.objects.order_by('service_ToBeDate')'''