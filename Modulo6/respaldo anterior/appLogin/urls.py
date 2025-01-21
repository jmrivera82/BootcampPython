from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


app_name='appLogin'

urlpatterns = [
    
    path('registro/', views.registro_view, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]