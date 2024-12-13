from django.shortcuts import render
from .forms import VehiculoForm

# Create your views here.

def index(request):
     return render(request, 'vehiculo/index.html')

#def registro(request):
#     return render(request, 'vehiculo/registro.html')

#PARTE 2
#Vista creada para instanciar un vehículo en auto
def vehiculo_add(request):
     if request.method == 'POST':
          auto = VehiculoForm(request.POST)
          if auto.is_valid():
               registro = auto.cleaned_data
               return render(request,"vehiculo/datos_ingresados.html", {"registro":registro})
     else:
          auto = VehiculoForm()
     
     return render(request, "vehiculo/registro.html",{"auto":auto})
