from .serializers import CartItemSerializer

def cart_response(user):
    queryset = user.cart_items.select_related('product').all()
    serializer = CartItemSerializer(queryset, many=True)
    total = sum(item.subtotal() for item in queryset)
    items_count = sum(item.quantity for item in queryset)
    return {
        'success': True,
        'data': {
            'items': serializer.data,
            'total': total,
            'items_count': items_count,
        }
    }

def error_response(code, message, status_code=400):
    return {
        'success': False,
        'error': {
            'code': code,
            'message': message
        },
        'status_code': status_code
    }
