from django.contrib import admin

from .models import (
    Entidad,
    DistritoFederal,
    DistritoLocal,
    Municipio,
    Seccion,
    StatusPusinex,
    PaperSize,
    Localidad,
    Revision,
    TAC
)


admin.site.register(Entidad)
admin.site.register(DistritoFederal)
admin.site.register(DistritoLocal)
admin.site.register(Municipio)
admin.site.register(Seccion)
admin.site.register(StatusPusinex)
admin.site.register(PaperSize)
admin.site.register(Localidad)
admin.site.register(TAC)
admin.site.register(Revision)
