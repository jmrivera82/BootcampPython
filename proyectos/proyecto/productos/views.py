from django.shortcuts import render, redirect
from .models import Proveedor, Visitas, Producto
from django.urls import reverse
from .forms import ProductoForm
from django.http import HttpResponse
# Create your views here.

def menu(request):

    return render(request,'productos/menu.html')


def ingresar_proveedor(request):
    if request.method == 'POST':
        nombre=request.POST['nombre']
        ciudad=request.POST['ciudad']
        pais=request.POST['pais']
       
        proveedor=Proveedor(nombre=nombre,ciudad=ciudad,pais=pais)

        proveedor.save()

        return redirect('/listar_proveedor')
            
    else:

        return render(request, 'productos/ingresar_proveedor.html')


def listar_proveedor(request):

    proveedores=Proveedor.objects.all()
    return render(request,'productos/listar_proveedor.html',{'proveedores':proveedores})


def actualizar_proveedor(request,pk):
    proveedor= Proveedor.objects.get(id=pk)

    context={
        'proveedor':proveedor
    }

    return render(request, 'productos/actualizar_proveedor.html', context)

def actualizarProveedor(request,pk):

    nombre=request.POST['nombre']
    ciudad=request.POST['ciudad']
    pais=request.POST['pais']

    proveedor=Proveedor.objects.get (id=pk)   
    proveedor.nombre=nombre
    proveedor.ciudad=ciudad 
    proveedor.pais=pais
    proveedor.save()
    return redirect('/listar_proveedor')


def eliminar_proveedor(request,pk):
    proveedor=Proveedor.objects.get(id=pk)

    if request.method=='POST':
        proveedor.delete()
        return redirect('/listar_proveedor')
    
    context = {'proveedor': proveedor}

    return render(request, 'productos/eliminar_proveedor.html',context)


#PRODUCTOS

def ingresar_producto(request):
    #return render(request, 'productos/ingresar_producto.html')

    if request.method == 'POST':
          prod = ProductoForm(request.POST)
          if prod.is_valid():
               registro =Producto(
                    nombre=prod.cleaned_data['nombre'],
                    codigo=prod.cleaned_data['codigo'],
                    categoria=prod.cleaned_data['categoria'],
                    proveedor=prod.cleaned_data['proveedor'],
                    f_registro=prod.cleaned_data['f_registro'],
                    p_costo=prod.cleaned_data['p_costo'],
                    p_venta=prod.cleaned_data['p_venta'],
               ) 
               
               registro.save()
               return render(request,"productos/producto_ingresado.html", {"registro":registro})
    else:
          prod = ProductoForm()
     
    return render(request, "productos/ingresar_producto.html",{"prod":prod})

def listado_de_productos(request):
     productos = Producto.objects.all() 
     return render(request, 'productos/listado_de_productos.html', {'productos': productos})

#TEST

def test(request):

    return render(request,'productos/test.html')
