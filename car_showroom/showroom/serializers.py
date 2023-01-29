from rest_framework import serializers

from showroom.models import Showroom


class ShowroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = (
            'id',
            'name',
            'locations',
        )


class ShowroomRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = (
            'id',
            'name',
            'info',
            'locations',
            'balance',
            'customers',
            'cars',
        )


class ShowroomCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Showroom
        fields = (
            'id',
            'name',
            'info',
            'locations',
            'balance',
            'customers',
            'cars',
        )


