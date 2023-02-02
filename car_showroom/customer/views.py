from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from customer.serializers import CustomerSerializer, OfferSerializer

from customer.models import Customer, Offer


class CustomerViewSet(ModelViewSet):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)


class OfferViewSet(ModelViewSet):

    serializer_class = OfferSerializer
    queryset = Offer.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)
