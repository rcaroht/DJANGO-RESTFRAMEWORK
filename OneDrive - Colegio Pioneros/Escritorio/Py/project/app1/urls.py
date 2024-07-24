

#Acá van las urls de la aplicación. El otro urls, tiene las urls del proyecto


# app1/urls.py
# app1/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BdRawDataOldViewSet, BdRawDataNewViewSet

router = DefaultRouter()
router.register(r'bd_raw_data_old', BdRawDataOldViewSet)
router.register(r'bd_raw_data_new', BdRawDataNewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

