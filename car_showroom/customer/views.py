from rest_framework.viewsets import ModelViewSet

from customer.models import Customer, Offer
from customer.serializers import CustomerSerializer, OfferSerializer


class CustomerViewSet(ModelViewSet):
    serializer_classes = {
        "list": CustomerSerializer,
        "retrieve": CustomerSerializer,
        "create": CustomerSerializer,
    }
    queryset = Customer.objects.filter(is_active=True).all()


class OfferViewSet(ModelViewSet):
    serializer_classes = {
        "list": OfferSerializer,
        "retrieve": OfferSerializer,
        "create": OfferSerializer,
    }
    queryset = Offer.objects.filter(is_active=True).all()