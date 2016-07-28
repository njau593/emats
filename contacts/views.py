from django.shortcuts import render
from .models import reachUs
from .forms import newsletter_form

# Create your views here.

def contacts(request):
    card=reachUs.objects.all()
    #context=RequestContext(request)
    if request.method=='POST':
        form=newsletter_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #return contacts(request)
        else:
            print (form.errors)

    else:
        form=newsletter_form()

    return render(request, 'pages/contacts.html', {
    'card':card, 'form':form
    })

'''form=newsletter_form(request.POST)
if form.is_valid():
    post=form.save()
    post.save()
else:
    form=newsletter_form()'''
