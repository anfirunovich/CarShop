from rest_framework import routers

from core.views import LocationViewSet, CarViewSet

router = routers.DefaultRouter()

router.register('locations', LocationViewSet, basename='location')
router.register('cars', CarViewSet, basename='car')

urlpatterns = router.urls
