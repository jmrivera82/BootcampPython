from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    pass
    #revisar choices para marca y categoria
    modelo=models.CharField(max_length=100)
    serial_carroceria=models.CharField(max_length=50)
    serial_motor=models.CharField(max_length=50)

    precio=models.IntegerField()
    fecha_de_creacion=models.DateField()
    fecha_de_modificacion=models.DateField()
