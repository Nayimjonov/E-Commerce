from django.contrib import admin
from .models import CartItem

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'subtotal_display')
    search_fields = ('user__username', 'product__title')
    list_filter = ('user',)

    def subtotal_display(self, obj):
        return obj.subtotal()
    subtotal_display.short_description = 'Сумма'
