from rest_framework import routers

from showroom.v1.views import ShowroomViewSet


router = routers.DefaultRouter()

router.register('showrooms', ShowroomViewSet, basename='showroom')

urlpatterns = router.urls
