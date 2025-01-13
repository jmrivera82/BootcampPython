from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre=models.CharField(max_length=255)

    def __str__(self):
        return f"Nombre: {self.nombre}"

    class Meta:
        db_table='laboratorio'


class DirectorGeneral(models.Model):
    nombre=models.CharField(max_length=255)
    laboratorio=models.ForeignKey(Laboratorio,on_delete=models.SET_NULL, blank=True,null=True)     
    
    def __str__(self):
        return f"Nombre: {self.nombre}"
    
    class Meta:
        db_table='director_general'
