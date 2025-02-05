from django.db import models
from django.contrib.auth.models import User

class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments") 
    contenido = models.TextField()  
    fecha = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.post}"
    

class Post(models.Model):
    titulo = models.CharField(max_length=200)  # Título del post
    contenido = models.TextField()  # Contenido del post
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return self.titulo