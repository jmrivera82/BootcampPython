
from django.db import models

from datetime import date

# Create your models here.
class Proveedor(models.Model):
    nombre=models.CharField(max_length=255)
    ciudad=models.CharField(max_length=50, default='Santiago')
    pais=models.CharField(max_length=50, default='Chile')
   
    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table='proveedor'


class Mercaderista(models.Model):
    nombre=models.CharField(max_length=255)
    proveedor=models.OneToOneField(Proveedor,on_delete=models.CASCADE,related_name='mercaderista')     
    telefono=models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre}"
    
    class Meta:
        db_table='mercaderista'

class Producto(models.Model):
    nombre=models.CharField(max_length=255)
    codigo=models.IntegerField()

    CATEGORIA_CHOICES=[
            ('SIN ASIGNAR','sin_asignar'),
            ('LACTEOS','lacteos'),
            ('ABARROTES','abarrotes'),
            ('ASEO','aseo'),
            ('FRUTAS','frutas'),
            ('VERDURAS','verduras'),
            ('LICORES','licores'),
            ('BEBIDAS','bebidas'),
            ('MASCOTAS','mascotas'),
            ('LIBRERIA','libreria'),
            ('CONGELADOS','congelados'),

        ]   

    categoria=models.CharField(max_length=50,choices=CATEGORIA_CHOICES,default='sin_asignar')
    proveedor=models.ForeignKey(Proveedor,on_delete=models.SET_NULL, blank=True,null=True)     
    f_registro=models.DateField(default=date(2015,1,1))
    p_costo=models.DecimalField(max_digits=12,decimal_places=2)
    p_venta=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return f"{self.nombre},{self.p_venta}"

    class Meta:
        db_table='productos'


class Visitas(models.Model):
    pagina=models.CharField(max_length=255)
    contador=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.contador} visitas"