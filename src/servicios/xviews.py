"""from django.shortcuts import render
from servicios.models import Servicio #Con esto importados desde la app servicio, el archivo models y de ahí la clase Servicio.
def servicios(request):
    servicios=Servicio.objects.all() #Se crea una variable con cualquier nombre y la instruccion que le sigue es una orden a DJANGO para que importe todos los objetos (servicios) de la clase Servicio
    return render(request, "servicios/servicios.html", {"servicios": servicios}) #Este último parametro es el nombre de la variable, dos puntos y servicios. Veamos en el template de servicios, el bucle creado para que recorra todos los servicios creados.
"""