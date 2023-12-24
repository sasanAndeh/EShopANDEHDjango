from django.urls import include, path
from core.view.views import index
urlpatterns = [ 
    path('',index),
]
