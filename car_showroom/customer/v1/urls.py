from rest_framework import routers

from customer.v1.views import CustomerViewSet, OfferViewSet

router = routers.DefaultRouter()

router.register('customers', CustomerViewSet, basename='customer')
router.register('offers', OfferViewSet, basename='offer')

urlpatterns = router.urls
