from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('book/',views.book,name='book'),
    path('palindromo/',views.palindromo,name='palindromo'),
    path('listbook/', views.listar,name='listar')
]
