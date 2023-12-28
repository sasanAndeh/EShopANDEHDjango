from django.urls import path

from .views.ProductDetails import product_detail
urlpatterns = [ 
    path('<slug:slug>', product_detail, name= 'product_detail'),
]
