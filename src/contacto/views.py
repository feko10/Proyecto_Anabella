from django.shortcuts import render, redirect
from .forms import formularioContacto
# Create your views here.
def contacto(request):
    formulario_contacto=formularioContacto() #En esta función se crea una variable que es igual a nuestro forms.py creado. Esto permite instanciar el formulario y que lo renderice luego al sition.
    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)
        #Habiendo activado el methodo POST en forms, acá decimos que si se requierió ese metodo, entonces el objeto construido aqui en la variable(formulario_contacto) tiene que cargar esa informacion de lo enviado por la clase creada en forms (FormularioContacto). el data=request.POST es la información que el usuario introduce.
        if formulario_contacto.is_valid():
            nombre=request.POST.get("Nombre")
            email=request.POST.get("Email")
            contenido=request.POST.get("Contenido")
            #Ahora, si la información previa es valida le pedimos que se guarde en las diferentes variables lo que el  usuario escribio en cada formulario que es lo que está escrito entre "". Por ejemplo que se guarde en nombre lo que el usuario escribio en "nombre".
            return redirect("/contacto/?valido")
            #Con esto le decimos a DJANGO que si se envia la info, retorne una redireccion que en este caso comienza con un simbolo ? y una palabra (por ejemplo valido) (este redirect hay que importarlo para que funcione). Luego hay que ir a contacto.html y decirle a django que si redirecciona a ese sitio "valido" nos arroje una leyenda.

    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})