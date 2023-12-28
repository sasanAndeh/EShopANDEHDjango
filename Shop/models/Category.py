
from django.contrib.auth.models import User
from django.db import models

class category(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField(max_length=70) 
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title