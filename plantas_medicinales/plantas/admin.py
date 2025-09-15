from django.contrib import admin
from .models import Planta, Sintoma

# Clase para personalizar cómo se ve el modelo Planta en el admin
class PlantaAdmin(admin.ModelAdmin):
    # Esto muestra más información en la lista de plantas
    list_display = ('nombre_comun', 'nombre_cientifico')
    # Esto añade una barra de búsqueda
    search_fields = ('nombre_comun', 'nombre_cientifico')
    # Organiza los campos en secciones lógicas
    fieldsets = (
        ('Datos Básicos', {
            'fields': ('nombre_comun', 'nombre_cientifico', 'imagen')
        }),
        ('Contenido Detallado', {
            'fields': ('definicion', 'usos', 'historia', 'advertencias', 'fuentes')
        }),
        ('Relaciones', {
            'fields': ('sintomas_tratados',)
        }),
    )
    # Mejora la selección de síntomas
    filter_horizontal = ('sintomas_tratados',)

# Clase para personalizar el modelo Sintoma
class SintomaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

# Registramos nuestros modelos con sus personalizaciones
admin.site.register(Planta, PlantaAdmin)
admin.site.register(Sintoma, SintomaAdmin)