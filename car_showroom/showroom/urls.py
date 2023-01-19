from rest_framework import routers

from showroom import views

router = routers.DefaultRouter()
router.register('showrooms', views.ShowroomViewSet, basename='showroom')

urlpatterns = router.urls
