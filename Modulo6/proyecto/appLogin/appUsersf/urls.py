#from django.shortcuts import reverse, redirect
from django.urls import path
from . import views

app_name="appUsersf"

urlpatterns=[
    path('login/', views.login_view, name="login"),
    path('home/', views.home_view, name="home"),
    path('logout/', views.logout_view, name="logout"),

]