from django.db import models

# Create your models here.
class Sala(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=False)
    tamaño = models.IntegerField(null=True, blank=True) #! Metros cuadrados
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    aforo = models.IntegerField(null=True, blank=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    identificador = models.IntegerField(blank=True, null=True)

class Reservacion(models.Model):
    usuario  = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, null=True, blank=True, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    personas = models.IntegerField(null=True, blank=True)