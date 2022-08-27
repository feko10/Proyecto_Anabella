from django.shortcuts import render
from blog.models import Post #Con esto importamos la clase Post del models.py y luego creamos una variable llamada posts igual a todos los objetos de la clase Post dentro de este views. Luego le pasamos al render como tercer argumentos pasamos un diccionario llamado posts igual a posts
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts}) #variable post igual a todos los objetos de la clase post, y el ctx (tercer argumento) es igual a cada elemento de post.
# Recordar que nuestra plantilla está dentro de la misma carpeta templates/blog de esta misma app. Por eso el blog/blog.
#AL TERMINAR ACÁ NOS VAMOS AL TEMPLATES BLOG.
