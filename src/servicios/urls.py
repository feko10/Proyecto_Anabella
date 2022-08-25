#ATENCION-->SE COPIA EL URLS DE LA APP PRINCIPAL Y SE PEGA ACA, BORRANDO EL PATH DE SERVICIOS ABAJO
#Para evitar usar el urls del proyecto general debemos crear un archivo urls en cada app como en este caso, e importar el directorio de urls del pryecto gral, salvo el admin (primer path). Ese queda en su estado original.
from django.urls import path
from . import views #Aca en lugar del punto estaba "ProyectoWebbApp", pero es mejor poner el . para que diga que importe de todos los lugares
from django.conf import settings
from django.conf.urls.static import static
#En estos dos últimos import, le decimos a DJANGO que desde la configuración de django importe las configuraciones de setting y los archivos estaticos. Especificamente en este último le decimos que busque, dentro de la configuración de urls, y dentro de ello el dir statics.
#En el caso del import de settings, importamos todo porque allí seleccionamos creamos las variables de las carpetas medias y deberían figurar acá también.
urlpatterns = [
    path('', views.servicios, name="Servicios"),
    
    #No es necesario poner "servicios" al path en este caso porque estamos dentro de la app servicios. Entonces la raiz queda así: " ", porque se entienda que la raiz es /servicios mismo
]


#urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Con este le decimos, que a urlpatterns, es decir la variable de arriba le agregue los archivos staticos dentro de setting.MEDIA_URL y le indicamos la raiz (document_root) que es igual al archivo settings y dentro de ella la variable mediaroot
#ESTO LO DEJAMOS SIN EFECTO PORQUE ESTAMOS DENTRO DE LA APP SERVICIOS Y NO ES NECESARIO ESTANDO ACA HACER UN PATH DIR.