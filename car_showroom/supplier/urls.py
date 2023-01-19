from rest_framework import routers

from supplier import views

router = routers.DefaultRouter()
router.register('suppliers', views.SupplierViewSet, basename='supplier')
router.register('cars', views.CarViewSet, basename='car')

urlpatterns = router.urls
