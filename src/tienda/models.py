from django.db import models

# Aca se crea los modelos de categorias de los productos y otro de los productos. Aca se hace el mapeo OMR.

class CategoriaProd(models.Model): #Clase que crea una tabla de categoría de productos
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #Esto hace que inserte de manera automática la fecha en la tabla, al crearla.
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:  #Sirve para definir el nombre tanto en singular como plural, nuestra categoría
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

        def __str__(self):
            return self.nombre #Metodo string para que devuelve el nombre de la categoría

class Produto(models.Model): #Es el model para productos
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) #Aca relacionamos las categorias con, la variable del mismo nombre de la clase CategoriaProd, y a su vez activamos el on_delete que establece que si se borra una categoría, se eliminan todos los productos afines.
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)#Recordar instalar la libreria "Pilow o algo asi". Acá decimos que se carga la imagen en directorio tienda, se permite espacios vacíos y en blanco.
    precio=models.FloatField #Permite ingresar valores en decimales
    disponibilidad=models.BooleanField(default=True) #Em campo booleano (disponble o no), y que por defecto sea afirmativo

    class Meta:  #Sirve para definir el nombre tanto en singular como plural, nuestra categoría
        verbose_name="Producto"
        verbose_name_plural="Productos"

