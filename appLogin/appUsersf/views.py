from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #para visualizar contenido estando logueado
from .forms import LoginForm

# Create your views here.

def login_view(request): #login_view para que no se confunda con el login que fue importado
    if request.method== "POST":
        form= LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("appUsersf:home")
            else:
                form.add_error(None, "Acceso no válido..")
    else:
        form=LoginForm()

    template="appUsersf/login.html"
    context={"form":form} 

    return render(request, template, context)        

@login_required(login_url="login")
def home_view(request):
    template = "appUsersf/home.html"
    return render(request, template)


def logout_view(request):
    logout(request)
    return redirect("appUsersf:login")



