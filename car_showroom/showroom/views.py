from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom
from showroom.serializers import ShowroomSerializer, ShowroomRetrieveSerializer


class ShowroomViewSet(ModelViewSet):
    serializer_classes = {
        "list": ShowroomSerializer,
        "retrieve": ShowroomRetrieveSerializer,
    }
    queryset = Showroom.objects.filter(is_active=True).all()
   