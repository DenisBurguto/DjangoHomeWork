from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('about/', views.about, name='about'),
    path('get-orders-by-client/', views.get_orders_by_client, name='get_orders_by_client'),
    path('all-client-orders/<int:client_id>/', views.all_client_orders, name='all_client_orders'),
    path('all-client-orders/<int:client_id>/<int:period>', views.all_client_orders, name='all_client_orders'),

    # path('products/', views.products, name='products'),
    # path('orders/', views.orders, name='orders')
]
