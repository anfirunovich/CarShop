from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom

from showroom.v1.serializers import ShowroomSerializer

from showroom.filters.balance_filter import ShowroomBalanceFilter


class ShowroomViewSet(ModelViewSet):

    serializer_class = ShowroomSerializer
    queryset = Showroom.objects.filter(is_active=True).all()

    filterset_class = ShowroomBalanceFilter

    permission_classes = (permissions.IsAuthenticated,)


