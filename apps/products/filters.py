from django_filters.rest_framework import FilterSet, NumberFilter, CharFilter
from .models import Product


class ProductFilter(FilterSet):
    category = NumberFilter(field_name="category_id")
    min_price = NumberFilter(field_name="price", lookup_expr="gte")
    max_price = NumberFilter(field_name="price", lookup_expr="lte")
    attributes = CharFilter(method="filter_attributes")

    def filter_attributes(self, queryset, name, value):
        import json
        try:
            attr_dict = json.loads(value)
            for key, val in attr_dict.items():
                queryset = queryset.filter(**{f"attributes__{key}": val})
        except json.JSONDecodeError:
            return queryset.none()
        return queryset

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'attributes']