from django.shortcuts import render, redirect
#from .forms import EmpleadoForm
from .models import Empleado
from django.utils import timezone
from django.db import IntegrityError, transaction
# Create your views here.

def index(request):
    return render(request,'crudApp/index.html')

#Para mejorar de acuerdo con evaluación 9 agregar fecha de ingreso al modelo.

def ingresar_emp(request):
    if request.method == 'POST':
        #id=request.POST['id'] --> se modificó el modelo para usar el id de django
        nombre=request.POST['nombre']
        correo=request.POST['correo']
        cargo=request.POST['cargo']
        #Evaluación 9
        f_ingreso=request.POST['f_ingreso'] #--> se modificó el default con la fecha de hoy

        if not f_ingreso:  
            f_ingreso = None 
        else:
            f_ingreso = timezone.datetime.strptime(f_ingreso, '%Y-%m-%d').date()

        sueldo=request.POST['sueldo']

        empleado=Empleado(nombre=nombre,correo=correo,cargo=cargo,f_ingreso=f_ingreso,sueldo=sueldo)

        empleado.save()

        return redirect('/crudApp/listar')
            
    else:

        return render(request, 'crudApp/ingresar.html')



def actualizar_emp(request,pk):
    empleado= Empleado.objects.get(id=pk)

    context={
        'empleado':empleado
    }

    #return render(request=request, template_name='actualizar.html',context=context)
    return render(request, 'crudApp/actualizar.html', context)

def actualizarEmpleado(request,pk):
    #id=request.POST['id']
    nombre=request.POST['nombre']
    correo=request.POST['correo']
    cargo=request.POST['cargo']
    sueldo=request.POST['sueldo']


    empleado=Empleado.objects.get (id=pk)   
    #empleado.id=id
    empleado.nombre=nombre
    empleado.correo=correo 
    empleado.cargo=cargo
    empleado.sueldo=sueldo
    empleado.save()
    return redirect('/crudApp/listar')

def eliminar_emp(request,pk):
    empleado=Empleado.objects.get(id=pk)

    if request.method=='POST':
        empleado.delete()
        return redirect('/crudApp/listar')
    
    context = {'empleado': empleado}

    return render(request, 'crudApp/eliminar.html',context)


def listar_emp(request):
    empleados=Empleado.objects.all()
    return render(request,'crudApp/listar.html',{'empleados':empleados})


def error(request):
    return render(request,'crudApp/error.html')