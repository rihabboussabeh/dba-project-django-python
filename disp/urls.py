from __future__ import unicode_literals
from django.urls import path
from . import views

app_name= 'disp'

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('home/(?P<name>\w+/(?P<password>\w+))/', views.index, name='index'),
    path('error', views.errorpage, name='errorpage'),
   

    
]
