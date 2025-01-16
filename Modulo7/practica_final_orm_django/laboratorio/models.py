from django.db import models

from datetime import date

# Create your models here.
class Laboratorio(models.Model):
    nombre=models.CharField(max_length=255)
    ciudad=models.CharField(max_length=50, default='Santiago')
    pais=models.CharField(max_length=50, default='Chile')

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        db_table='laboratorio'


class DirectorGeneral(models.Model):
    nombre=models.CharField(max_length=255)
    laboratorio=models.OneToOneField(Laboratorio,on_delete=models.CASCADE,related_name='director_general')     
    especialidad=models.CharField(max_length=100, default='Sin asignar')

    def __str__(self):
        return f"Nombre:{self.nombre}"
    
    class Meta:
        db_table='director_general'

class Producto(models.Model):
    nombre=models.CharField(max_length=255)
    laboratorio=models.ForeignKey(Laboratorio,on_delete=models.SET_NULL, blank=True,null=True)     
    f_fabricacion=models.DateField(default=date(2015,1,1))
    p_costo=models.DecimalField(max_digits=12,decimal_places=2)
    p_venta=models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
        return f"{self.nombre},{self.p_venta}"

    class Meta:
        db_table='productos'


class Visitas(models.Model):
    pagina=models.CharField(max_length=255)
    contador=models.IntegerField()

    def __str__(self):
        return f"{self.contador} visitas"