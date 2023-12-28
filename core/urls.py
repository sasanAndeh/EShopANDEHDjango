from django.urls import include, path
from core.view.Index import index
from core.view.About import about


urlpatterns = [ 
    path('',index, name='index'),
    path('about' , about,name='about'),
]
