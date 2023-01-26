from rest_framework.viewsets import ModelViewSet

from showroom.models import Car

from supplier.serializers import SupplierSerializer, CarSerializer


class SupplierViewSet(ModelViewSet):
    serializer_classes = {
        "list": SupplierSerializer,
        "retrieve": SupplierSerializer,
        "create": SupplierSerializer,
    }
    queryset = Car.objects.filter(is_active=True).all()


class CarViewSet(ModelViewSet):
    serializer_classes = {
        "list": CarSerializer,
        "retrieve": CarSerializer,
        "create": CarSerializer,
    }
    queryset = Car.objects.filter(is_active=True).all()
