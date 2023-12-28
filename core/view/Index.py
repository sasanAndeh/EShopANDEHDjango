from django.shortcuts import render , HttpResponse


from Shop.models.Product import product
# Create your views here.

def index(request):
    products = product.objects.all()[0:6]
    return render(request , 'core/index.html',{ 'products':products })
