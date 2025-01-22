from django.db import models
from django.conf import settings

# Create your models here.

class Permisos(models.Model):

    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.titulo