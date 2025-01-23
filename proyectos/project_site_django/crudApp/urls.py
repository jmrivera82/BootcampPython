from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),

    path('ingresar/',views.ingresar_emp,name='ingresar_emp'),
    path('listar/',views.listar_emp,name='listar_emp'),
    path('actualizar/<int:pk>',views.actualizar_emp,name='actualizar_emp'),
    path('actualizar/actualizarEmpleado/<int:pk>',views.actualizarEmpleado,name='actualizarEmpleado'),

    path('eliminar/<int:pk>',views.eliminar_emp,name='eliminar_emp'), 
    path('error/',views.error,name='error'),

]