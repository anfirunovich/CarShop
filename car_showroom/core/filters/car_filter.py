from core.models import Car

from django_filters import FilterSet, NumberFilter


class CarFilter(FilterSet):
    max_engine_power = NumberFilter(field_name='engine_power', lookup_expr='gt')
    min_engine_power = NumberFilter(field_name='engine_power', lookup_expr='lt')

    max_year = NumberFilter(field_name='year', lookup_expr='gt')
    min_year = NumberFilter(field_name='year', lookup_expr='lt')

    class Meta:
        model = Car
        fields = (
            'engine_power',
            'max_engine_power',
            'min_engine_power',
            'year',
            'max_year',
            'min_year',
        )



