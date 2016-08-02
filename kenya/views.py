from django.shortcuts import render
from .models import kenyaInfo
from django.shortcuts import render, get_object_or_404

# Create your views here.

def info(request):
    kinfo=kenyaInfo.objects.all()
    return render(request, 'pages/kenya.html', {'kinfo':kinfo})

def kenya_detail(request, pk):
    det_kenya=get_object_or_404(kenyaInfo, pk=pk)
    return render(request, 'pages/kenya_detail.html', {
    'det_kenya':det_kenya
    })
