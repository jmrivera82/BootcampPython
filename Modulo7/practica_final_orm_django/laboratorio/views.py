from django.shortcuts import render, redirect
from .models import Laboratorio, Visitas
from django.urls import reverse
# Create your views here.

def index(request):

    return render(request,'laboratorio/index.html')


def ingresar(request):
    if request.method == 'POST':
        nombre=request.POST['nombre']
        ciudad=request.POST['ciudad']
        pais=request.POST['pais']
       
        labo=Laboratorio(nombre=nombre,ciudad=ciudad,pais=pais)

        labo.save()

        return redirect('/listar')
            
    else:

        return render(request, 'laboratorio/ingresar.html')


def listar(request):

    laboratorio=Laboratorio.objects.all()
    return render(request,'laboratorio/listar.html',{'laboratorio':laboratorio})

    #Agregar un contador para la vista listar

    #pagina='listar'
    #cuenta, creado = Visitas.objects.get_or_create(pagina=pagina)

    #if creado:
    #    print("Se creó un nuevo registro para la página.")
    #else:
    #    print("Se encontró un registro existente para la página.")


    #cuenta.contador+=1
    #cuenta.save()

    #laboratorio=Laboratorio.objects.all()

    #context = {
    #    'laboratorios': laboratorio,
    #    'contador': cuenta.contador,
    #}

    #return render(request,'laboratorio/listar.html',context)

def actualizar(request,pk):
    laboratorio= Laboratorio.objects.get(id=pk)

    context={
        'laboratorio':laboratorio
    }

    return render(request, 'laboratorio/actualizar.html', context)

def actualizarLaboratorio(request,pk):

    nombre=request.POST['nombre']
    ciudad=request.POST['ciudad']
    pais=request.POST['pais']

    laboratorio=Laboratorio.objects.get (id=pk)   
    laboratorio.nombre=nombre
    laboratorio.ciudad=ciudad 
    laboratorio.pais=pais
    laboratorio.save()
    return redirect('/listar')


def eliminar(request,pk):
    laboratorio=Laboratorio.objects.get(id=pk)

    if request.method=='POST':
        laboratorio.delete()
        return redirect('/listar')
    
    context = {'laboratorio': laboratorio}

    return render(request, 'laboratorio/eliminar.html',context)