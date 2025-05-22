from django.urls import path
from . import views

urlpatterns = [
    path('shop/products/', views.ProductListView.as_view(), name='list'),

]