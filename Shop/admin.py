from django.contrib import admin
from .models.Product import product
from .models.Category import category


# Register your models here.

admin.site.register(product)
admin.site.register(category)