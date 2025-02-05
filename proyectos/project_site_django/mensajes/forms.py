from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Escribe tu comentario...'}),
        }