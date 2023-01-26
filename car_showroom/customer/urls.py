from rest_framework import routers

from customer.views import CustomerViewSet, OfferViewSet


router = routers.DefaultRouter()

router.register('customers', CustomerViewSet, base_name='customer')
router.register('offers', OfferViewSet, base_name='offer')

urlpatterns = router.urls
