from django.contrib import admin
from .models import *


class ColegioAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "direccion", "telefono")


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("documento", "primer_nombre", "primer_apellido", "segundo_apellido")


class PuntuacionAdmin(admin.ModelAdmin):
    list_display = ("estudiante", "puntuacion", "fecha")


class CursoAdmin(admin.ModelAdmin):
    list_display = ("grado", "salon", "colegio")
# Register your models here.
admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Estudiante, PersonaAdmin)
admin.site.register(Puntuacion, PuntuacionAdmin)
admin.site.register(Docente, PersonaAdmin)
admin.site.register(Curso, CursoAdmin)