from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .paginations import ProductPagination
from .utils import success_response, error_response
from .filters import ProductFilter


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at', 'title', 'average_rating']
    ordering = ['title']


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
        except Http404:
            return error_response("id", "Product not found", http_status=status.HTTP_404_NOT_FOUND)
        return success_response(self.get_serializer(obj).data)
