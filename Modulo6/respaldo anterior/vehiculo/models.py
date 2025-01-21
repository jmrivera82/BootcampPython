from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    #Parte 1 práctica de consolidación

    MARCA_CHOICES=[
        ('FIAT','Fiat'),
        ('CHEVROLET','Chevrolet'),
        ('FORD','Ford'),
        ('TOYOTA','Toyota')
       ]
    
    marca=models.CharField(max_length=20, choices=MARCA_CHOICES,default='Ford')
    modelo=models.CharField(max_length=100)
    serial_carroceria=models.CharField(max_length=50)
    serial_motor=models.CharField(max_length=50)

    CATEGORIA_CHOICES=[
        ('PARTICULAR','Particular'),
        ('TRANSPORTE','Transporte'),
        ('CARGA','Carga'),
       ]
    
    categoria=models.CharField(max_length=20,choices=CATEGORIA_CHOICES,default='Particular')
    precio=models.IntegerField()
    fecha_de_creacion=models.DateField()
    fecha_de_modificacion=models.DateField()

    def traer_condicion_de_precio (self):

        if self.precio < 10000:
            return "Bajo"
        elif self.precio > 30000:
            return "Alto"
        else:
            return "Medio"

    def __str__(self):
        return f"{self.marca} {self.modelo}"

    #creación de permiso visualizar catalogo

    class Meta:
        db_table='vehiculos'
        permissions = [
            ("visualizar_catalogo", "Puede visualizar el catálogo de vehículos"), ("add_vehiculomodel", "Puede agregar los vehículos")
        ]

    #Parte 4 obtener cndición de precio y pasar al listado según condición

