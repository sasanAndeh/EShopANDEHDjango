
from datetime import datetime    
from django.contrib.auth.models import User
from django.db import models
from .Category import category
class product(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField(max_length=70) 
    description = models.TextField(blank=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    user  = models,models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(category,related_name='products', on_delete=models.CASCADE)
    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self) -> str:
        return self.title
    def get_display_price(self):
        return "{:_}".format(self.price)