"""
Definition of views.
"""

from .models import DistritoFederal, Municipio
from rest_framework import viewsets
from rest_framework import permissions
from datetime import datetime
from django.views.generic import TemplateView
from .serializers import (
    DistritoFederalSerializer,
    MunicipioSerializer)


class Home(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Home, self).get_context_data(*args,**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context


class DistritoFederalSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los Distritos Federales
    """
    queryset = DistritoFederal.objects.all()
    serializer_class = DistritoFederalSerializer


class MunicipioSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los Municipio
    """
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
