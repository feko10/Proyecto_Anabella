#Para realizar un formulario hay que crear un archivo como esto. luego importar from django forms y luego una clase con el nombre del formulario que queremos y que reciba de parametros forms.Form.
from django import forms

class formularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True) #Se crea los diferentes campos. La variable nombre es igual a un campo de caracteres cuyo nombre es "nombre" y el required True exige que se haga complete el campo.
    email=forms.CharField(label="Email", required=True)
    contenido=forms.CharField(label="Contenido")

