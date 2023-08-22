"""
URL configuration for rentalcar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rentalcar import settings
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
#views
from internal.views import CarViewSet, SignUpViewSet, CurrentUserViewSet, BrandViewSet

router = routers.SimpleRouter()
router.register(r'signup', SignUpViewSet)
router.register(r'currentuser', CurrentUserViewSet)
router.register(r'cars', CarViewSet)
router.register(r'brands', BrandViewSet)
api = r'^api/'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Rental Car",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(api, include('drf_social_oauth2.urls', namespace='drf')),
    re_path(api,include('rest_framework.urls')),
    re_path(api, include(router.urls)),
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('sentry-debug/', trigger_error),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
