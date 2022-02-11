from email.policy import default
from django import forms

class ClientesFormulario (forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class VendedorFormulario (forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    legajo = forms.IntegerField()

class VehiculoFormulario (forms.Form):

    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    añofabricacion = forms.IntegerField()
    disponible = forms.BooleanField(initial=True)