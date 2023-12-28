from django.contrib import admin

# Register your models here.
from .models.UserProfile import userprofile

admin.site.register(userprofile)