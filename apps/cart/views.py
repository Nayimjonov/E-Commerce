from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import CartItem
from products.models import Product
from .responses import cart_response, error_response


class CartBaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get_cart_data(self):
        return cart_response(self.request.user)


class CartView(CartBaseView):
    def get(self, request):
        data = self.get_cart_data()
        return Response(data)


class AddToCartView(CartBaseView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        if not product_id:
            return Response({'success': False, 'error': {'message': 'product_id обязателен'}},
                            status=status.HTTP_400_BAD_REQUEST)

        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        data = self.get_cart_data()
        return Response(data)


class CartDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):
        try:
            cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
            cart_item.delete()
        except CartItem.DoesNotExist:
            error = error_response('NOT_FOUND', 'Product not found in cart', status_code=status.HTTP_404_NOT_FOUND)
            return Response(error, status=error['status_code'])

        data = cart_response(request.user)
        return Response(data)
