from rest_framework import serializers

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    slug = serializers.CharField()


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    thumbnail = serializers.URLField()
    category = CategorySerializer()
    average_rating = serializers.FloatField()
    likes_count = serializers.IntegerField()


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    images = serializers.ListField(
        child=serializers.URLField()
    )
    category = CategorySerializer()
    attributes = serializers.DictField(
        child=serializers.CharField()
    )
    average_rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    likes_count = serializers.IntegerField()
    is_liked = serializers.BooleanField()
    in_stock = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
