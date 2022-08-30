#Para evitar usar el urls del proyecto general debemos crear un archivo urls en cada app como en este caso, e importar el directorio de urls del pryecto gral, salvo el admin (primer path). Ese queda en su estado original.
#from xml.etree.ElementInclude import include
from django.urls import path, include
from django.contrib import admin
from . import views #Aca en lugar del punto estaba "ProyectoWebbApp", pero es mejor poner el . para que diga que importe de todos los lugares
from django.conf import settings
from django.conf.urls.static import static
#from ProyectoWebApp import views
#from django.conf import settings
#from django.conf.urls.static import static
#En estos dos últimos import, le decimos a DJANGO que desde la configuración de django importe las configuraciones de setting y los archivos estaticos. Especificamente en este último le decimos que busque, dentro de la configuración de urls, y dentro de ello el dir statics.
#En el caso del import de settings, importamos todo porque allí seleccionamos creamos las variables de las carpetas medias y deberían figurar acá también.

urlpatterns = [

    path('', views.home, name="Home"), #Aca llamamos las urls y en el sengundo parametros las vinculamos con las views de de la app importada. comillas vacias porque no se tiene nombre de inicio y el nombre será "name" será equivalente al de las diferentes views importadas. Luego irá el views, punto más nombre de la función de la app en views.

    path('tienda', views.tienda, name="Tienda"),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Con este le decimos, que a urlpatterns, es decir la variable de arriba le agregue los archivos staticos dentro de setting.MEDIA_URL y le indicamos la raiz (document_root) que es igual al archivo settings y dentro de ell"a la variable mediaroot"""

"""path('admin/', admin.site.urls), 
    path('servicios/', include('servicios.urls')), #el include quiere decir que se incluyan todos los path que hay en urls de la app servicios
    path('', include('ProyectoWebApp.urls')), 
"""