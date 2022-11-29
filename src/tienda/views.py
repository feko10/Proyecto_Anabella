from django.shortcuts import render
from .models import Producto

def tienda(request):

    productos=Producto.objects.all()
    #Se crea una variable donde se almacene la lista de productos desde models y lo renderice en el sitio para, para que se vea en "tienda". 
    return render(request, "tienda/tienda.html", {"productos":productos})
#Para renderizar en el sitio, siempre se usa el tercer parametro que es el contexto y es un diccionario con la variable creada arriba. Es lo mismo que hicimos en blog.