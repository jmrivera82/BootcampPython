from django.contrib import admin
from django.urls import path
from . import views

app_name='productos'

urlpatterns = [

    path('menu_productos/',views.menu,name='menu'),
    path('ingresar_proveedor/',views.ingresar_proveedor,name='ingresar_proveedor'),
    path('listar_proveedor/',views.listar_proveedor,name='listar_proveedor'),
    path('actualizar_proveedor/<int:pk>',views.actualizar_proveedor,name='actualizar_proveedor'),
    path('actualizar_proveedor/actualizarProveedor/<int:pk>',views.actualizarProveedor,name='actualizarProveedor'),
    path('eliminar_proveedor/<int:pk>',views.eliminar_proveedor,name='eliminar_proveedor'), 
    path('ingresar_producto/',views.ingresar_producto,name='ingresar_producto'),
    path('listado_de_productos/',views.listado_de_productos,name='listado_de_productos'),
    path('productos/test/',views.test,name='test'),


]