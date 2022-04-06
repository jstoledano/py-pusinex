"""
Definition of models.
"""

from django.db import models


class Entidad(models.Model):
    entidad = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.entidad:02d} - {self.nombre.upper()}'


class Distrito(models.Model):
    distrito = models.PositiveIntegerField(primary_key=True)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    cabecera = models.CharField(max_length=100)

    def __str__(self) -> str:
        distrito = f'{self.entidad.entidad:02d}{self.distrito:02d} - {self.cabecera.upper()}'
        return distrito
