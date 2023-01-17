from rest_framework.viewsets import ModelViewSet

from showroom.models import Showroom


class ShowroomView(ModelViewSet):
    serializer_classes = {
        "list": ShowroomSerializer,
        "retrieve": ShowroomRetrieveSerializer,
        "create": ShowroomCreateSerializer,
    }
    queryset = Showroom.objects.filter(is_active=True).all()
   