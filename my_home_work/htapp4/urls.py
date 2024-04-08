from django.urls import path
from . import views

urlpatterns = [
    path('get-product-by-id/', views.get_product_by_id, name='get_product_by_id'),
    path('get-product-by-id/<str:success_message>', views.get_product_by_id, name='get_product_by_id'),
    path('product-update/<int:product_id>/', views.product_update, name='product_update'),
]
