from django.contrib import admin
from .models import Categoria, Post #Con el . indicamos que el archivo está dentro del mismo directorio, luego importamos los clases de views.

#Con esta variable le decimos a Django que lea dos registros de nuestra BD que no aparece porque son de "solo lectura"
# Register your models here. Aca registramos la app de servicios para que aparezca luego en el url /admin/. 
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'update')
    #Con esta variable le decimos a Django que lea dos registros de nuestra BD que no aparece porque son de "solo lectura"

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
#Con esto se registra el modelo de models creado para que aparezca en admin, tanto los registros de la tabla servicio, como los que son de solo lectura que no aparecen si no es usando la clase de arriba.
# Luego de esto entramos en el sitio, usando la barra /admin/, nos logueamos y nos va aparecer la sección servicios donde figurarían las tablas creadas con la base de datos.