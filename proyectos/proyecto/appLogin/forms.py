from django import forms
#from .models import BoardsModel
# Agregando para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Agregado para el registro de usuarios
class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']                        
        if commit:
            user.save()
        return user