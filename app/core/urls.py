from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Meant4 API",
      default_version='Showcase API',
      description="API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


swaggerpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('meant.urls'))

] + swaggerpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)








