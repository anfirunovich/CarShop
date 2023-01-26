from rest_framework import serializers

from showroom.models import Showroom
from supplier.models import Car


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = (
            'id',
            'name',
            'info',
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'id',
            'manufacturer',
            'brand',
            'description',
            'year',
            'color',
            'type',
            'engine_power',
            'transmission',
            'price',
        )

