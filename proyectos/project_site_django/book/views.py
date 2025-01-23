from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro


# Create your views here.

#Sesion 4 Ejercicio

def index (request):
    return render(request,'book/index.html')

def book (request):
    return HttpResponse("Bienvenido a mi sitio de libros")

#Sesión 5 Ejercicio

def palindromo(request, palabra):
    palabra = palabra.lower().replace(" ", "")
    resultado = palabra == palabra[::-1]
    return render(request, "palindromo.html", {"palabra": palabra, "resultado": resultado})

#Ejercicio sesion 6

def listar (request):
    libros=Libro.objects.all()
    return render(request, "book/listbook.html",{'libros':libros})