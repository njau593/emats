from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.products, name='products'),
    url(r'^products/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^products/readmore/(?P<pk>\d+)/$', views.actual_product, name='actual_product'),
]
