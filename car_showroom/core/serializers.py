from rest_framework import serializers

from core.models import Car, Location


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


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'country',
            'city',
            'street',
            'house_number',
        )
