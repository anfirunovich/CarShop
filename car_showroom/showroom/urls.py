from rest_framework import routers

from showroom.views import ShowroomViewSet, LocationViewSet


router = routers.DefaultRouter()

router.register('showrooms', ShowroomViewSet, base_name='showroom')
router.register('locations', LocationViewSet, base_name='location')

urlpatterns = router.urls