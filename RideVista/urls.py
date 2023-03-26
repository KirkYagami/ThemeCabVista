from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('ride', views.ride, name= 'ride'),
    path('success/', views.success, name= 'success')
    
]