from django import forms

class VehiculoForm(forms.Form):
        MARCA_CHOICES=[
        ('FIAT','Fiat'),
        ('CHEVROLET','Chevrolet'),
        ('FORD','Ford'),
        ('TOYOTA','Toyota')
       ]
    
        marca=forms.ChoiceField(choices=MARCA_CHOICES)
        modelo=forms.CharField(max_length=100)
        serial_carroceria=forms.CharField(max_length=50)
        serial_motor=forms.CharField(max_length=50)

        CATEGORIA_CHOICES=[
            ('PARTICULAR','Particular'),
            ('TRANSPORTE','Transporte'),
            ('CARGA','Carga'),
        ]
        
        categoria=forms.ChoiceField(choices=CATEGORIA_CHOICES)
        precio=forms.IntegerField()
        fecha_de_creacion=forms.DateField()
        fecha_de_modificacion=forms.DateField()
