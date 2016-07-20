from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name='home'),
    #url(r'^products/$', views.products, name='products'),
    url(r'^about/$', views.about, name='about'),
    #url(r'^contacts/$', views.contacts, name='contacts'),
]
