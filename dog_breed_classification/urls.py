from django.urls import path,include
from . import views
from django.conf.urls import url



urlpatterns=[
    path('dog_breed_api/',views.model,name='dog_breed_api'),
    #path('convert/',views.convert,name='convert')
    url(r'^convert/$',views.convert,name='convert'),
    
]
