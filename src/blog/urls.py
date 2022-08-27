#Se crea primero el archivo urls.py y se hace las importaciones. CUANDO TERMINAMOS ACÁ NOS VAMOS A URLS GENERAL DEL PROYECTO.
from django.urls import path
from . import views #Aca en lugar del punto estaba "ProyectoWebbApp", pero es mejor poner el . para que diga que importe de todos los lugares
"""from django.conf import settings
from django.conf.urls.static import static
#En estos dos últimos import, le decimos a DJANGO que desde la configuración de django importe las configuraciones de setting y los archivos estaticos. Especificamente en este último le decimos que busque, dentro de la configuración de urls, y dentro de ello el dir statics.
#En el caso del import de settings, importamos todo porque allí seleccionamos creamos las variables de las carpetas medias y deberían figurar acá también."""
urlpatterns = [
    path('blog', views.blog, name="Blog"),
]