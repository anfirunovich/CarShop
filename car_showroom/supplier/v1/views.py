from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from supplier.v1.serializers import SupplierSerializer

from supplier.models import Supplier


class SupplierViewSet(ModelViewSet):

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)
