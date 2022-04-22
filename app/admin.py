from django.contrib import admin

from .models import (
    Entidad,
    DistritoFederal,
    DistritoLocal,
    Municipio,
    Seccion,
    StatusPusinex,
    PaperSize,
    Localidad
)


admin.site.register(Entidad)
admin.site.register(DistritoFederal)
admin.site.register(DistritoLocal)
admin.site.register(Municipio)
admin.site.register(Seccion)
admin.site.register(StatusPusinex)
admin.site.register(PaperSize)
admin.site.register(Localidad)
