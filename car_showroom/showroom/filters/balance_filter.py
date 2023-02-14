from showroom.models import Showroom

from django_filters import FilterSet, NumberFilter


class ShowroomBalanceFilter(FilterSet):
    max_balance = NumberFilter(field_name='balance', lookup_expr='gt')
    min_balance = NumberFilter(field_name='balance', lookup_expr='lt')

    class Meta:
        model = Showroom
        fields = (
            'balance',
            'min_balance',
            'max_balance',
        )
