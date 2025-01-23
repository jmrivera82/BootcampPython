from django.db import models
from datetime import date

# Create your models here.

   #Evaluación 9 agregaré el sueldo y la fecha de ingreso al modelo
   #f_ingreso=models.DateField() se reemplazó por algomas automático
   #se cambió la base de datos a practica_crud ya que las migraciones no ingresaban las columnas f_ingreso y sueldo

class Empleado(models.Model):
   
   nombre=models.CharField(max_length=255)
   correo=models.EmailField()
   cargo=models.CharField(max_length=150)
   f_ingreso=models.DateField(default=date.today) #Gracias ChatGPT el modelo necesitaba asignar la fecha de ingreso automaticamente.
   sueldo=models.DecimalField(max_digits=12,decimal_places=2,default='500000')

   def __str__(self):
       return f"Nombre: {self.nombre} - {self.cargo},{self.correo}"

   #class Meta:
   #    db_table='crudapp_empleado'
   

