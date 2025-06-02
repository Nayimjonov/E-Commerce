from django.urls import path
from . import views

urlpatterns = [
    path('shop/cart/', views.CartView.as_view(), name='cart-view'),
    path('cart/<int:product_id>/', views.CartDeleteView.as_view(), name='cart-delete'),
]
