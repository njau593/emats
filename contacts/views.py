from django.shortcuts import render
from .models import reachUs
from .forms import news_form
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import context

# Create your views here.

def contacts(request):
    card=reachUs.objects.all()
    '''form=newsletter_form(request.POST)
    if form.is_valid():
        post=form.save()
        post.save()
    else:
        form=newsletter_form()'''

    form_class=news_form
    if request.method == 'POST':
        form=form_class(data=request.POST)

        if form.is_valid():
            sub_name=request.POST.get('sub_name', '')
            sub_email=request.POST.get('sub_email', '')
            form_content=request.POST.get('content', '')

            #Email the profile with the contact information
            template=get_template('contact_template.txt')
            example=context({
                'sub_name':sub_name,
                'sub_email':sub_email,
                #'form_content':form_content,
            })
            content=template.render(example)

            email=EmailMessage(
                "New contact form submission",
                content,
                "Your website"+'',
                ['njaugodfrey@outlook.com'],
                headers={ 'Reply-To':sub_email }
            )
            email.send()
            return redirect('contacts')

    return render(request, 'pages/contacts.html', {
    'card':card, 'form':form_class
    })
