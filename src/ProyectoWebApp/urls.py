#Para evitar usar el urls del proyecto general debemos crear un archivo urls en cada app como en este caso, e importar el directorio de urls del pryecto gral, salvo el admin (primer path). Ese queda en su estado original.
from django.urls import path
from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"), #Aca llamamos las urls y en el sengundo parametros las vinculamos con las views de de la app importada. comillas vacias porque no se tiene nombre de inicio y el nombre será "name" será equivalente al de las diferentes views importadas. Luego irá el views, punto más nombre de la función de la app en views.
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]