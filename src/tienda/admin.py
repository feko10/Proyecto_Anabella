from django.contrib import admin
from .models import CategoriaProd, Producto
# Importamos desde modelos, las clases creadas en models.

# Ahora, debemos decirle a DJANGO que las categorias creadas, són de solo lectura con la class que se crea abajo.

class CategoriaProdAdmin(admin.ModelAdmin): #Esto hereda de admin, modelAdmn
    readonly_fields=("created", "updated") #Con esto indicamos los campos de solo lectura

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields =("created", "updated") #Idem arriba

admin.site.register(CategoriaProd, CategoriaProdAdmin) #Con esto se vincula y registra las categorias y productos tanto del Admin, como abajo del producto
admin.site.register(Producto, ProductoAdmin)
#Ver como se hizo en la parte de BLOG, es lo mismo. Luego ver en el la barra del sitio /admin y vamos a poder ver la nueva categoria