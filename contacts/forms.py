from django import forms
from .models import newsletter

class newsletter_form(forms.ModelForm):
    class Meta:
        model=newsletter
        fields=['Name', 'Email',]

'''class news_form(forms.Form):
    sub_name=forms.CharField(max_length=100, required=False)
    sub_email=forms.EmailField(required=True)'''
