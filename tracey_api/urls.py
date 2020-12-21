
from django.contrib import admin
from django.urls import path, include
from rest_framework import viewsets, routers
from main_app.views import RegistrationAPI, ContactUsAPI


router = routers.DefaultRouter()
router.register('register', RegistrationAPI, basename='register')
router.register('contact_us', ContactUsAPI, basename='contact_us')
    




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
