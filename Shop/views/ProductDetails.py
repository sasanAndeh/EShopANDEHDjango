from django.shortcuts import render ,get_object_or_404
from Shop.models.Product import product

def product_detail(request,slug ):
    pro = get_object_or_404(product, slug = slug)
    return render(request,'shop/product_detail.html',{'product':pro})
