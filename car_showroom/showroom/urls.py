from rest_framework import routers

from showroom.views import ShowroomViewSet


router = routers.DefaultRouter()

router.register('showrooms', ShowroomViewSet, basename='showroom')

urlpatterns = router.urls
