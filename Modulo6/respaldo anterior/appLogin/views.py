from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import RegistroUsuarioForm
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#def registro_view(request): prueba de render y direccionamiento
#    return render(request,'appLogin/registro.html')


def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado exitosamente" )
            #return HttpResponseRedirect('/login')
            return redirect('appLogin:login')    

        messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")

    else:

        form = RegistroUsuarioForm()

    return render (request=request, template_name="appLogin/registro.html",context={"register_form":form})

def login_view(request):

    form = AuthenticationForm(request, data=request.POST)

    if request.method == "POST":

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                #return HttpResponseRedirect('/menu')
                return redirect('vehiculo:index')    


            messages.error(request,"Invalido username o password.")
    
        else:

            messages.error(request,"Invalido username o password.")

    return render(request, 'appLogin/login.html', {'login_form':form})

def logout_view(request):
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")

    logout(request)

    return redirect('vehiculo:index')    
