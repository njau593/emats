from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^kenya/$', views.info, name='info'),
    url(r'^kenya/(?P<pk>\d+)/$', views.kenya_detail, name='kenya_detail'),
]
