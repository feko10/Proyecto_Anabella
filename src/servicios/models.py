from email.headerregistry import ContentDispositionHeader
from django.db import models

# Create your models here.
class Servicio(models.Model): #Se crea una clase, y esa clase como tal hereda desde models.Model.
    titulo=models.CharField(max_length=100) #Aca nombramos un registro (titulo) y le asignamos un tipo de valor (cuadro de texto -Charfield-)
    contenido=models.CharField(max_length=900)
    imagen=models.ImageField(upload_to='servicios') #Este campo upload_to sirve para que cuando se cargue una imagen, se suba a la carpeta que indicamos dentro de "media" que se designo en settings. No es necesario crear la carpeta servicios previamente, si la de media.
    created=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de creacion de servicio. En este caso se toma de models, un campo de feha y se agrega como argumento ese código que sirve para que tome la fecha automaticamente al momento del registro.
    #VER EN SETTINGS, URL MEDIA Y ROOT MEDIA QUE SE CREO ABAJO DE TODO. LUEGO CHEQUEAR QUE EN URLS ESTÉ TODO BIEN PARA QUE NO DE ERROR.
    update=models.DateTimeField(auto_now_add=True) #Campos que sirven para orden la fecha de actualización servicio
    
    class Meta: 
        verbose_name="servicio"
        verbose_name_plural="servicios"
    
    def __str__(self):
        return self.titulo

    """Estos son los diferentes campos que tendrá el registro de la BD de que hay en esta clase.
    De manera opcional se puede agregar los META, en la que existe una clase Meta.
    Primero se crea una clase propia nuestra como la de arriba, y dentro se hace una clase interna llamada Meta con sus propias especificaciones.
     También se puede usar el verbose_name que especifica el nombre que va a tener el nombre del modelo de la BD como de los campos, pero en nuestro caso ya lo hemos hecho con código. 
     Luego, fuera de la clase interna, se crea una función tipo str, para que devuelva un texto y retorne (en este caso) la variable título.
     Finalmente hay que hacer las migraciones para que esto aparezca en nuestra BD"""