from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom, Location

from showroom.serializers import (
    ShowroomSerializer,
    ShowroomRetrieveSerializer,
    ShowroomCreateSerializer,
    LocationSerializer
)


class ShowroomViewSet(ModelViewSet):
    serializer_classes = {
        "list": ShowroomSerializer,
        "retrieve": ShowroomRetrieveSerializer,
        "create": ShowroomCreateSerializer,
    }
    queryset = Showroom.objects.filter(is_active=True).all()


class LocationViewSet(ModelViewSet):
    serializer_classes = {
        "list": LocationSerializer,
        "retrieve": LocationSerializer,
        "create": LocationSerializer,
    }
    queryset = Location.objects.filter(is_active=True).all()