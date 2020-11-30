
from django.contrib import admin
from django.urls import path, include
from rest_framework import  viewsets, routers

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main_app.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
