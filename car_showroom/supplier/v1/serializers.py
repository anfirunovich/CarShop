from rest_framework import serializers

from showroom.models import Showroom


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = (
            'id',
            'name',
            'info',
        )


