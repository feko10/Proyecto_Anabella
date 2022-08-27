from email.headerregistry import ContentDispositionHeader
from django.db import models
from django.contrib.auth.models import User #Con esta clase podemos utilizar el uso de varios usuarios en las diferentes clases.
# Create your models here.
class Categoria(models.Model): #Se crea una clase, y esa clase como tal hereda desde models.Model.
    nombre=models.CharField(max_length=50) #Aca nombramos un registro (nombre) y le asignamos un tipo de valor (cuadro de texto -Charfield-)
    created=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de creacion de servicio. En este caso se toma de models, un campo de fecha y se agrega como argumento ese código que sirve para que tome la fecha automaticamente al momento del registro.
    #VER EN SETTINGS, URL MEDIA Y ROOT MEDIA QUE SE CREO ABAJO DE TODO. LUEGO CHEQUEAR QUE EN URLS ESTÉ TODO BIEN PARA QUE NO DE ERROR.
    update=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de actualización servicio

    class Meta: 
        verbose_name="categoria"
        verbose_name_plural="categorias"

         
    def __str__(self):
        return self.nombre
    
class Post(models.Model): 
    titulo=models.CharField(max_length=50) #Aca nombramos un registro (titulo) y le asignamos un tipo de valor (cuadro de texto -Charfield-)
    contenido=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True) #Este campo upload_to sirve para que cuando se cargue una imagen, se suba a la carpeta que indicamos dentro de "media" que se designo en settings. No es necesario crear la carpeta servicios previamente, si la de media. EL NULL Y BLANK = TRUE, signfica que el ingreso de imagen es opcional y no obligatorio!
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #Con la creación de esta variable se pide que el autor, que pertence a un FK, al borrarlo, borre todos sus modelos en cascada (sus blogs basicamente)
    categorias=models.ManyToManyField(Categoria) #Con esto creamos un campo que relaciona esta clase, con la de Categorias, en una relación de varios a varios, es decir, varios posts, pueden pertenecer a varias categorias
    created=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de creacion de servicio. En este caso se toma de models, un campo de feha y se agrega como argumento ese código que sirve para que tome la fecha automaticamente al momento del registro.
    #VER EN SETTINGS, URL MEDIA Y ROOT MEDIA QUE SE CREO ABAJO DE TODO. LUEGO CHEQUEAR QUE EN URLS ESTÉ TODO BIEN PARA QUE NO DE ERROR.
    update=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de actualización servicio

    class Meta: 
        verbose_name="post"
        verbose_name_plural="posts"

   