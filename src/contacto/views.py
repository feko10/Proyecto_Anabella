from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from Anabella import settings
# Create your views here.
def contacto(request):
    formulario_contacto=formularioContacto() #En esta función se crea una variable que es igual a nuestro forms.py creado. Esto permite instanciar el formulario y que lo renderice luego al sitio.
    
    if request.method=="POST":
        formulario_contacto=formularioContacto(data=request.POST)
        #Habiendo activado el methodo POST en forms, acá decimos que si se requierió ese metodo, entonces el objeto construido aqui en la variable(formulario_contacto) tiene que cargar esa informacion de lo enviado por la clase creada en forms (FormularioContacto). el data=request.POST es la información que el usuario introduce.
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            telefono=request.POST.get("telefono")
            contenido=request.POST.get("contenido")
             #Ahora, si la información previa es valida le pedimos que se guarde en las diferentes variables lo que el usuario escribio en cada formulario que es lo que está escrito entre "". Por ejemplo que se guarde en nombre lo que el usuario escribio en "nombre".
            email=EmailMessage("Mensaje desde Sitio Web Anabella-Nutrición", "El usuario nombre {} con la dirección {}. Telefono {}, escribe lo siguiente:\n\n {}".format(nombre,email,telefono,contenido), "",["fkozakgrassini@gmail.com"],reply_to=[email])
            

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
           #Con esto se nos enviará un e-mail, que se configuró en "settings.py", para que el sitio nos mandé un correo con la info que el cliente puso en el formulario.
           #A su vez en los últimos parametros colocamos nuestro correo electronico que gestionará la recepción de esa info y el envío y el reply_to que es para que conteste lo recibido, y que recibirá entre [] el argumento del email que el cliente consignó en el form.
            #---return redirect("/contacto/?valido")---
            #Con esto le decimos a DJANGO que si se envia la info, retorne una redireccion que en este caso comienza con un simbolo ? y una palabra (por ejemplo valido) (este redirect hay que importarlo para que funcione). Luego hay que ir a contacto.html y decirle a django que si redirecciona a ese sitio "valido" nos arroje una leyenda.

    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})


"""
def contacto(request):
    form = formularioContacto()
    
    if request.method=="POST":
        form = formularioContacto(request.POST or None)
        if form.is_valid():
            subject="asunto… "
            message=request.POST["mensaje"] #mensaje
            email_from=settings.EMAIL_HOST_USER #los mails se envían
        email_to=["fkozakgrassini@gmail.com"] # a este
        send_mail(subject, message, email_from, email_to)
    return render(request, "contacto.html")"""