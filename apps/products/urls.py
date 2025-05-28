from django.urls import path
from . import views

urlpatterns = [
    path('shop/products/', views.ProductListView.as_view(), name='list'),
    path('shop/products/<int:pk>/', views.ProductDetailView.as_view(), name='list'),

]
