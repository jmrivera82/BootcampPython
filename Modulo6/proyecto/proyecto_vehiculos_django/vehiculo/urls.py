from django.urls import path
from . import views

app_name="vehiculo"

urlpatterns=[
    path('', views.index, name="index"),
]