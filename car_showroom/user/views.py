from rest_framework import viewsets, permissions

from user.serializers import UserSerializer

from user.models import User


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    permission_classes = (permissions.IsAuthenticated,)
