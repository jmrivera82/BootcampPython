from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm (AuthenticationForm): #clase que hereda de AuthenticationForm
    #atributos
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
