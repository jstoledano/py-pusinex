"""
Definition of models.
"""

from django.db import models
from django.db.models import UniqueConstraint

TIPO_SECCION = (
    ('U', 'Urbana'),
    ('R', 'Rural'),
    ('M', 'Mixta')
)


class Entidad(models.Model):
    entidad = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Entidades'
        verbose_name = 'Entidad'

    def __str__(self) -> str:
        return f'{self.entidad:02d} - {self.nombre.upper()}'


class DistritoFederal(models.Model):
    distrito_federal = models.PositiveIntegerField(primary_key=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidad_distrito')
    cabecera = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Distritos Federales'
        verbose_name = 'Distrito Federal'

    def __str__(self) -> str:
        distrito = f'{self.entidad.entidad:02d}{self.distrito_federal:02d} - {self.cabecera.upper()}'
        return distrito


class DistritoLocal(models.Model):
    distrito_local = models.PositiveIntegerField(primary_key=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidad_distrito_local')
    cabecera = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Distritos Locales'
        verbose_name = 'Distrito Local'

    def __str__(self) -> str:
        distrito = f'{self.entidad.entidad:02d}{self.distrito_local:02d} - {self.cabecera.upper()}'
        return distrito


class Municipio(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidad_municipio')
    municipio = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Municipios'
        verbose_name = 'Municipio'

    def __str__(self) -> str:
        municipio = f'{self.entidad.entidad:02d}{self.municipio:03d} - {self.nombre.upper()}'
        return municipio


class Seccion(models.Model):
    entidad = models.ForeignKey(
        Entidad, on_delete=models.CASCADE,
        related_name='entidad_seccion', default=29)
    distrito_federal = models.ForeignKey(
        DistritoFederal,
        on_delete=models.CASCADE,
        related_name='distrito_federal_seccion')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_seccion')
    seccion = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TIPO_SECCION)

    class Meta:
        verbose_name_plural = 'Secciones'
        verbose_name = 'Sección'

    def __str__(self) -> str:
        seccion = f'{self.entidad.entidad:02d} {self.distrito_federal.distrito_federal:02d} {self.seccion:04d}'
        return seccion


class StatusPusinex(models.Model):
    status = models.CharField(max_length=1, primary_key=True)
    descripcion = models.CharField("Descripción", max_length=100)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados de PUSINEX"

    def __str__(self):
        return self.descripcion


class PapperSize(models.Model):
    tipo = models.CharField(max_length=1, primary_key=True)
    size = models.CharField("Tamaño", max_length=3)
    descripcion = models.CharField("Descripción", max_length=25)

    class Meta:
        verbose_name = "Tamaño"
        verbose_name_plural = "Tamaños de Papel"

    def __str__(self):
        return self.descripcion


class Localidad(models.Model):
    id = models.AutoField(primary_key=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="localidad_seccion")
    localidad = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'Localidades'
        constraints =[
            UniqueConstraint(fields=['seccion', 'localidad'], name='idxLocalidad'),
        ]

    def __str__(self):
        return f'{self.seccion:04d}: {self.localidad:04d} - {self.nombre}'
