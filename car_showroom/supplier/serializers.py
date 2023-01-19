from rest_framework import serializers

from supplier.models import Supplier, Car


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
        )


class SupplierRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
            'info',
            'foundation_date',
        )


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            "name",
            "description",
            "year",
            "color",
            "type",
            "price",
        )


