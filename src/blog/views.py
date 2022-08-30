from django.shortcuts import render
from blog.models import Post, Categoria #Con esto importamos la clase Post del models.py y luego creamos una variable llamada posts igual a todos los objetos de la clase Post dentro de este views. Luego le pasamos al render como tercer argumentos pasamos un diccionario llamado posts igual a posts
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts}) #variable post igual a todos los objetos de la clase post, y el ctx (tercer argumento) es igual a cada elemento de post.
# Recordar que nuestra plantilla está dentro de la misma carpeta templates/blog de esta misma app. Por eso el blog/blog.
#AL TERMINAR ACÁ NOS VAMOS AL TEMPLATES BLOG.

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria,"posts": posts})
#Esta función se vinculará a categorias.html y además del request, usa como parametro el nombre de alguna columna de la base de datos que queremos que tome.
#Luego creamos una variable (categoria) que tome de la clase categoria sus objetos, pero filtrados (get) por categoria id.
#Después creamos otra variable que sea igual a todos los posts, pero filtrado por la variable categoria.
#Luego le ponemos que nos devuelva todo eso, es decir, el tipico request, dentro de la urls que creamos al respecto, filtrado por categoría y por posts correspondientes a esas categorias  en su ctx. VER URLS