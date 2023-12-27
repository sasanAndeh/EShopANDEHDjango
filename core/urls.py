from django.urls import include, path
from core.view.Index import index
from core.view.About import about


urlpatterns = [ 
    path('',index),
    path('about' , about),
]
