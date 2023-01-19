from rest_framework.viewsets import ModelViewSet

from customer.models import Customer

from customer.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = {
        "list": CustomerSerializer,
    }
    queryset = Customer.objects.filter(is_active=True).all()

