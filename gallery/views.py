from django.shortcuts import render
from .models import pictures

# Create your views here.

def photos(request):
    picha=pictures.objects.order_by('-Photo_date')
    return render(request, 'pages/gallery.html', {'picha':picha})
