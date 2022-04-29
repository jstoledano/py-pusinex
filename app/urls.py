from django.urls import include, path
from rest_framework import routers
from .views import (
    Home,
    DistritoFederalSet,
    MunicipioSet,
    SeccionSet)


router = routers.DefaultRouter()
router.register(r'df', DistritoFederalSet)
router.register(r'mpio', MunicipioSet)
router.register(r'secc', SeccionSet)

app_name = 'pusinex'
urlpatterns = [
    path("", Home.as_view(), name='index'),
    path('api/', include(router.urls))
]