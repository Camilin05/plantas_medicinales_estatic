from django.db import models

class Sintoma(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción general del síntoma.")
    recomendaciones = models.TextField(blank=True, null=True, help_text="Advertencias o recomendaciones para tratar este síntoma, como 'Usar solo en casos leves'.")

    def __str__(self):
        return self.nombre

class Planta(models.Model):
    # --- DATOS BÁSICOS ---
    nombre_comun = models.CharField(max_length=100)
    nombre_cientifico = models.CharField(max_length=100, unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='plantas_imagenes/', blank=True, null=True, help_text="Sube una imagen de la planta.")

    # --- CONTENIDO DETALLADO ---
    definicion = models.TextField(blank=True, null=True, help_text="Corresponde a la sección 'DEFINICIÓN' de tu archivo.")
    usos = models.TextField(blank=True, null=True, help_text="Corresponde a la sección 'USOS', describe cómo aplicar la planta.")
    historia = models.TextField(blank=True, null=True, help_text="Corresponde a la sección 'HISTORIA' de la planta.")
    fuentes = models.TextField(blank=True, null=True, help_text="Pega aquí los links a estudios o fuentes de información.")
    
    # --- NUEVO CAMPO DE ADVERTENCIAS ---
    advertencias = models.TextField(blank=True, null=True, help_text="Contraindicaciones importantes, como 'No usar durante el embarazo o lactancia'.")

    # --- RELACIÓN CON SÍNTOMAS ---
    sintomas_tratados = models.ManyToManyField(Sintoma, related_name="plantas_recomendadas")

    def __str__(self):
        return self.nombre_comun