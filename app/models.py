"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
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
    distrito_federal = models.ForeignKey(
        DistritoFederal,
        on_delete=models.CASCADE,
        related_name='distrito_federal_seccion')
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='municipio_seccion')
    seccion = models.PositiveIntegerField(primary_key=True)
    tipo = models.CharField(max_length=1, choices=TIPO_SECCION)

    class Meta:
        verbose_name_plural = 'Secciones'
        verbose_name = 'Secci??n'

    def __str__(self) -> str:
        seccion = f'{self.distrito_federal.distrito_federal:02d} {self.seccion:04d}'
        return seccion


class StatusPusinex(models.Model):
    status = models.CharField(max_length=1, primary_key=True)
    descripcion = models.CharField("Descripci??n", max_length=100)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados de PUSINEX"

    def __str__(self):
        return self.descripcion


class PaperSize(models.Model):
    tipo = models.CharField(max_length=1, primary_key=True)
    size = models.CharField("Tama??o", max_length=3)
    descripcion = models.CharField("Descripci??n", max_length=25)

    class Meta:
        verbose_name = "Tama??o"
        verbose_name_plural = "Tama??os de Papel"

    def __str__(self):
        return self.descripcion


class Localidad(models.Model):
    id = models.IntegerField(primary_key=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name="localidad_seccion")
    localidad = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=1)

    class Meta:
        verbose_name_plural = 'Localidades'
        constraints = [
            UniqueConstraint(fields=['seccion', 'localidad'], name='idxLocalidad'),
        ]

    def __str__(self):
        return f'{self.seccion.seccion:04d}: {self.localidad:04d} - {self.nombre}'


class Pusinex(models.Model):
    id = models.IntegerField(primary_key=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name="pusinex_localidad")
    status_pusinex = models.ForeignKey(StatusPusinex, on_delete=models.CASCADE, related_name="pusinex_status")
    fecha_levantamiento = models.DateField()

    def __str__(self) -> str:
        return f'{self.localidad.seccion.seccion:04d} ' \
               f'{self.localidad.localidad:04d} ' \
               f'{self.localidad.nombre} ' \
               f'({self.fecha_levantamiento})'


class TAC(models.Model):
    distrito = models.ForeignKey(DistritoFederal, on_delete=models.CASCADE)
    nombre = models.TextField(max_length=150)
    clave = models.TextField(max_length=4)

    class Meta:
        verbose_name = "T??cnico Cart??grafo"
        verbose_name_plural = "T??cnicos"

    def __str__(self):
        return f'{self.distrito.distrito_federal:02d} - {self.clave}'


# Funci??n para subir archivos
def subir_documento(instancia, archivo):
    import os.path
    ext = archivo.split('.')[-1]
    dto = instancia.pusinex.localidad.seccion.distrito_federal.distrito_federal
    mpio = instancia.pusinex.localidad.seccion.municipio.municipio
    secc = instancia.pusinex.localidad.seccion.seccion
    loc = instancia.pusinex.localidad.localidad
    rev = instancia.revision
    hoja = instancia.hoja
    nombre = f'PUSINEX_29{dto:02}-{mpio:03d}-{secc:04d}-{loc:04d}-R{rev:02d}H{hoja:02d}.pdf'
    ruta = os.path.join('media','pusinex', f'Distrito {dto:02d}', nombre)
    return ruta


class Revision(models.Model):
    pusinex = models.ForeignKey(Pusinex, on_delete=models.CASCADE)
    revision = models.PositiveSmallIntegerField()
    hoja = models.PositiveSmallIntegerField()
    fecha_act = models.DateField()
    archivo = models.FileField(upload_to=subir_documento, blank=True, null=True)
    tac = models.ForeignKey(TAC, on_delete=models.CASCADE)
    # Trazabilidad
    autor = models.ForeignKey(User, related_name='revisions_user', editable=False, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'PUSINEX_29{self.pusinex.localidad.seccion.distrito_federal.distrito_federal:02d}-\
        {self.pusinex.localidad.seccion.municipio.municipio:03d}-{self.pusinex.localidad.seccion.seccion:04d}-\
        {self.pusinex.localidad.localidad:04d}-R{self.revision:02d}H{self.hoja:02d}'
