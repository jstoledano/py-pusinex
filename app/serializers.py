# coding: utf-8

from .models import (DistritoFederal,
                     Municipio,
                     Seccion,
                     Localidad)
from rest_framework import serializers


class DistritoFederalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DistritoFederal
        fields = ['distrito_federal', 'cabecera']


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = ['municipio', 'nombre']


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ['distrito_federal', 'municipio', 'seccion', 'tipo']


class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = ['id', 'seccion', 'localidad', 'nombre', 'tipo']