from car_showroom import settings

from car_showroom.yasg import urlpatterns as swagger_urls

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('showroom/', include('showroom.v1.urls')),
    path('customer/', include('customer.v1.urls')),
    path('supplier/', include('supplier.v1.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

if settings.USE_SWAGGER:
    urlpatterns += swagger_urls
