from django.shortcuts import render, HttpResponse


# Create your views here. Aca van las diferentes funciones que tendrá esta aplicación.
#ORM -> mapeo de objeto relacional. Se crea un codigo que representa una tabla de BD. Es una forma de eventualmente se pueda, con un código vincular a python con una tabla y registro de BD. Esto se crea en los archivos models.py
"""def home(request):
    return HttpResponse("home")
    
def servicios(request):
    return HttpResponse("servicios") 

def blog(request):
    return HttpResponse("blog") 

def contacto(request):
    return HttpResponse("contacto") 

def tienda(request):
    return HttpResponse("tienda")"""  


def home(request):
    return render(request, "ProyectoWebApp/home.html")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")

"""def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, "ProyectoWebApp/servicios.html", {"servicios": servicios})

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")
#SE CORTO LA FUNCION DE SERVICIOS Y SE LA LLEVÓ A UN ARCHIVO VIEWS.PY DENTRO DE LA APP SERVICIOS"""


    
"""
#Terminado esa parte inicial, vamos a crear una carpeta templates en ProyectoWebApp y luego una subcarpeta con el mismo nombre de nuestra app que ya mencionamos. Luego hacemos los html de cada función.
#Para que nuestras apps funciones recordar de ir settings, en nuestro archivo base, ir a INSTALLED_APPS y agregar la app respectiva.
#Una vez creada la carpeta de templates, debemos hacer que nuestras funciones de esta página las rendericen. Para eso invocamos las función render por cada template y la vinculamos en cada función.
"""