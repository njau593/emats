from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^kenya/$', views.info, name='info'),
]
