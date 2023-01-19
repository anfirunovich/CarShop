from django_filters import FilterSet, NumberFilter

from supplier.models import Car


class CarFilter(FilterSet):
    max_price = NumberFilter(field_name='price', lookup_expr='gte')
    min_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Car
        fields = (
            "max_price",
            "min_price",
        )
