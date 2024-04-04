from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('about/', views.about, name='about'),
    # path('clients/', views.clients, name='clients'),
    # path('products/', views.products, name='products'),
    # path('orders/', views.orders, name='orders')
]
