from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('ingresar/',views.ingresar,name='ingresar'),
    path('listar/',views.listar,name='listar'),
    path('actualizar/<int:pk>',views.actualizar,name='actualizar'),
    path('actualizar/actualizarLaboratorio/<int:pk>',views.actualizarLaboratorio,name='actualizarLaboratorio'),
    path('eliminar/<int:pk>',views.eliminar,name='eliminar'), 



]