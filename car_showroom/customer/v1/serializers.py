from rest_framework import serializers

from customer.models import Customer, Offer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'first_name',
            'last_name',
            'sex',
            'phone_number',
            'balance',
            'user_id',
        )


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = (
            'id',
            'customer',
            'car',
            'max_price',
        )
