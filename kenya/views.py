from django.shortcuts import render
from .models import kenyaInfo

# Create your views here.

def info(request):
    kinfo=kenyaInfo.objects.all()
    return render(request, 'pages/kenya.html', {'kinfo':kinfo})
