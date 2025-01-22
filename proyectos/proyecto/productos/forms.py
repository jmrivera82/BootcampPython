from django import forms 
from datetime import date
from . models import Proveedor

class ProductoForm(forms.Form):
        nombre=forms.CharField(max_length=255)
        codigo=forms.IntegerField()

        CATEGORIA_CHOICES=[
            ('SIN ASIGNAR','sin_asignar'),
            ('LACTEOS','lacteos'),
            ('ABARROTES','abarrotes'),
            ('ASEO','aseo'),
            ('FRUTAS','frutas'),
            ('VERDURAS','verduras'),
            ('LICORES','licores'),
            ('BEBIDAS','bebidas'),
            ('MASCOTAS','mascotas'),
            ('LIBRERIA','libreria'),
            ('CONGELADOS','congelados'),

        ]   

        categoria=forms.ChoiceField(choices=CATEGORIA_CHOICES)
        proveedor=forms.CharField()     
        f_registro=forms.DateField()
        p_costo=forms.DecimalField(max_digits=12,decimal_places=2)
        p_venta=forms.DecimalField(max_digits=12,decimal_places=2)