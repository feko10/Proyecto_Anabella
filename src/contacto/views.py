from django.shortcuts import render
from .forms import formularioContacto
# Create your views here.
def contacto(request):
    formulario_contacto=formularioContacto() #En esta función se crea una variable que es igual a nuestro forms.py creado. Esto permite instanciar el formulario y que lo renderice luego al sition.
    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})