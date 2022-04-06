"""
Definition of models.
"""

from django.db import models


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
    cabecera = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Municipios'
        verbose_name = 'Municipio'

    def __str__(self) -> str:
        municipio = f'{self.entidad.entidad:02d}{self.municipio:03d} - {self.nombre.upper()}'
        return municipio


class Seccion(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='entidad_seccion')
    distrito_federal = models.ForeignKey(
        DistritoFederal,
        on_delete=models.CASCADE,
        related_name='distrito_federal_seccion')
    distrito_local = models.ForeignKey(
        DistritoLocal,
        on_delete=models.CASCADE,
        related_name='distrito_local_seccion')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_seccion')
    seccion = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TIPO_SECCION)

    class Meta:
        verbose_name_plural = 'Secciones'
        verbose_name = 'Sección'

    def __str__(self) -> str:
        seccion = f'{self.entidad.entidad:02d} {self.distrito_federal.distrito_federal:02d} {self.seccion:04d}'
        return seccion
