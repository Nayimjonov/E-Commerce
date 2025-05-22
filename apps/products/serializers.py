from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.FloatField()
    thumbnail = serializers.URLField()
    average_rating = serializers.FloatField()
    likes_count = serializers.IntegerField()
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        c = obj.category
        return {
            "id": c.id,
            "name": c.name,
            "slug": c.slug,
        }
