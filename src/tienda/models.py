from django.db import models

# Aca se crea los modelos de categorias de los productos y otro de los productos. Aca se hace el mapeo OMR.

class CategoriaProd(models.Model): #Clase que crea una tabla de categoría de productos
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #Esto hace que inserte de manera automática la fecha en la tabla, al crearla.
    updated=models.DateTimeField(auto_now_add=True)
#En defintiva, estos campos muestran cuando se creo un producto y cuándo se actualizó. Esto luego debe replicarse en la clase que crea productos (Class producto) y finalmente hacer un migrate.

    class Meta:  #Sirve para definir el nombre tanto en singular como plural, nuestra categoría
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        
        return self.nombre #Metodo string para que devuelve el nombre de la categoría en el panel admin y sitio

class Producto(models.Model): #Es el model para productos
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) #Aca relacionamos las categorias con, la variable del mismo nombre de la clase CategoriaProd, y a su vez activamos el on_delete que establece que si se borra una categoría, se eliminan todos los productos afines.
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)#Recordar instalar la libreria "Pilow o algo asi". Acá decimos que se carga la imagen en directorio tienda, se permite espacios vacíos y en blanco.
    precio=models.FloatField() #Permite ingresar valores en decimales
    disponibilidad=models.BooleanField(default=True) #Em campo booleano (disponble o no), y que por defecto sea afirmativo.
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True)
#Se copian las dos sentencias de arriba para incorpararlas 

    class Meta:  #Sirve para definir el nombre tanto en singular como plural, nuestra categoría
        verbose_name="Producto"
        verbose_name_plural="Productos"



"""HECHO ESTO EL PROCEDIMIENTO ES MUY PARECIDO COMO EN EL CASO DEL BLOG
DEBIENDO IR ENTONCES AL ARCHIVO ADMIN DE LA "TIENDA"
"""

"""TAMBIEN DEBEMOS IR AL HTML DE TIENDA Y COPIAR LO MISMO QUE HAY EN BLOG O SERVICIOS, 
AJUSTANDO EN DICHO HTML LO NECESARIO. ESTO ES SOLO PARA VER QUE FUNCIONE PORQUE LUEGO VAMOS A BORRAR ESO Y 
ARMAR NUEVA PLANTILLA"""


"""TAMBIEN DEBEMOS DAR UN FORMATO ESPECIAL EN ESTA TIENDA.
SI VAMOS AL ARCHIVO BASE.HTML, AHI AL PRINCIPIO SE CARGA UNA PLANTILLA STACTIC DE BOOTSTRAP.CSS QUE
ESTA DENTRO DE LA CARPETA STATICS, VENDOR Y "CSS" Y"""