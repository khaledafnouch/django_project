from django.urls import path
from . import  views

urlpatterns = [
  path('', views.index, name='index'),
  path('contact/', views.contact, name='contact'),
  path('services/', views.services, name='services'),
  path('about/', views.about, name='about'),
  path('produits/', views.produits, name='produits'),
  path('produits/<int:pk>', views.detail, name='detail'),
  
  ]