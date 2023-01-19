from rest_framework import routers

from customer import views

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename='customer')

urlpatterns = router.urls

