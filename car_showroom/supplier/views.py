from rest_framework.viewsets import ModelViewSet

from supplier.filters.car_filters import CarFilter

from supplier.models import Supplier, Car

from supplier.serializers import SupplierSerializer, CarSerializer, SupplierRetrieveSerializer


class SupplierViewSet(ModelViewSet):

    serializer_class = {
        "list": SupplierSerializer,
        "retrieve": SupplierRetrieveSerializer,
    }
    queryset = Supplier.objects.filter(is_active=True).all()


class CarViewSet(ModelViewSet):

    serializer_class = {
        "list": CarSerializer,
        "retrieve": CarSerializer,
    }
    queryset = Car.objects.filter(is_active=True).all()
    filter_class = CarFilter
