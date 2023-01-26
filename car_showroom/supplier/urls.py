from rest_framework import routers

from supplier.views import SupplierViewSet, CarViewSet


router = routers.DefaultRouter()

router.register('suppliers', SupplierViewSet, base_name='supplier')
router.register('cars', CarViewSet, base_name='car')

urlpatterns = router.urls
