from django.urls import include, path
from rest_framework import routers
from .views import (Home,
                    DistritoFederalSet,
                    MunicipioSet,
                    SeccionSet,
                    LocalidadSet,
                    DistritoFederalList, DistritoFederalDetail)


router = routers.DefaultRouter()
router.register(r'df', DistritoFederalSet)
router.register(r'mpio', MunicipioSet)
router.register(r'secc', SeccionSet)
router.register(r'loc', LocalidadSet)

app_name = 'pusinex'
urlpatterns = [
    path("", Home.as_view(), name='index'),
    path("distrito/", DistritoFederalList.as_view()),
    path("distrito/<int:pk>", DistritoFederalDetail.as_view()),
    path('api/', include(router.urls))
]