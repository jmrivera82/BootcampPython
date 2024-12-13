from django.urls import path
from . import views

app_name="vehiculo"

urlpatterns=[
    path('', views.index, name="index"),
    path('add/', views.vehiculo_add, name="vehiculo_add"),

]