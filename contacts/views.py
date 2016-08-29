from django.shortcuts import render
from .models import reachUs
#from .forms import newsletter_form

# Create your views here.

def contacts(request):
    card=reachUs.objects.all()

    return render(request, 'pages/contacts.html', {
    'card':card
    })
