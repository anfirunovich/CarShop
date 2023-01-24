from supplier.models import Car

from django_filters import FilterSet, NumberFilter


class CarFilter(FilterSet):
    max_price = NumberFilter(field_name='price', lookup_expr='gt')
    min_price = NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Car
        fields = (
            'manufacturer',
            'brand',
            'price',
            'min_price',
            'max_price',
        )
