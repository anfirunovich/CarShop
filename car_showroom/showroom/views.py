from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom

from showroom.serializers import (
    ShowroomRetrieveSerializer,
    ShowroomCreateSerializer,
    ShowroomSerializer,
)


class ShowroomViewSet(ModelViewSet):

    default_serializer_class = ShowroomSerializer
    serializer_classes = {
        "list": ShowroomSerializer,
        "retrieve": ShowroomRetrieveSerializer,
        "create": ShowroomCreateSerializer,
    }

    queryset = Showroom.objects.filter(is_active=True).all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
