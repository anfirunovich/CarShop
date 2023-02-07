from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from core.serializers import CarSerializer, LocationSerializer

from core.models import Car, Location


class CarViewSet(ModelViewSet):

    serializer_class = CarSerializer
    queryset = Car.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)


class LocationViewSet(ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)