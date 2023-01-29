from rest_framework import routers

from supplier.views import SupplierViewSet


router = routers.DefaultRouter()

router.register('suppliers', SupplierViewSet, basename='supplier')

urlpatterns = router.urls
