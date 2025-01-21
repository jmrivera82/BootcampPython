from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
     return render(request, 'vehiculo/index.html')

#def registro_vehiculo(request):
#     return render(request, "vehiculo/registro.html")

@login_required
def vehiculo_list(request):
     return render(request, 'vehiculo/listado.html')

#PARTE 2
#Vista creada para instanciar un vehículo en auto

def vehiculo_add(request):
     if request.method == 'POST':
          auto = VehiculoForm(request.POST)
          if auto.is_valid():
               registro =Vehiculo(
                    marca=auto.cleaned_data['marca'],
                    modelo=auto.cleaned_data['modelo'],
                    serial_carroceria=auto.cleaned_data['serial_carroceria'],
                    serial_motor=auto.cleaned_data['serial_motor'],
                    categoria=auto.cleaned_data['categoria'],
                    precio=auto.cleaned_data['precio'],
                    fecha_de_creacion=auto.cleaned_data['fecha_de_creacion'],
                    fecha_de_modificacion=auto.cleaned_data['fecha_de_modificacion'],
               ) 
               
               registro.save()
               return render(request,"vehiculo/datos_ingresados.html", {"registro":registro})
     else:
          auto = VehiculoForm()
     
     return render(request, "vehiculo/registro.html",{"auto":auto})

#PARTE 4 - Creación de vista para el listado de vehículoss
#Se requeire importar el modelo Vehículo creado en la parte 1



def vehiculo_list(request):
     vehiculos = Vehiculo.objects.all() 
     return render(request, 'vehiculo/listado.html', {'vehiculos': vehiculos})