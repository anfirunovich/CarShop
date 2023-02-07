from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom

from showroom.v1.serializers import ShowroomSerializer


class ShowroomViewSet(ModelViewSet):

    serializer_class = ShowroomSerializer
    queryset = Showroom.objects.filter(is_active=True).all()

    permission_classes = (permissions.IsAuthenticated,)


