from rest_framework import serializers


class ProductShortSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    thumbnail = serializers.ImageField()


class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(write_only=True, required=False)
    product = ProductShortSerializer(read_only=True)
    quantity = serializers.IntegerField()
    subtotal = serializers.SerializerMethodField()

    def get_subtotal(self, obj):
        return float(obj.subtotal())

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductShortSerializer(instance.product).data
        representation['subtotal'] = self.get_subtotal(instance)
        return representation

    def to_internal_value(self, data):
        validated = super().to_internal_value(data)
        return validated

