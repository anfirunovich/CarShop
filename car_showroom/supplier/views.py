from rest_framework.viewsets import ModelViewSet

from supplier.serializers import SupplierSerializer

from supplier.models import Supplier


class SupplierViewSet(ModelViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.filter(is_active=True).all()

