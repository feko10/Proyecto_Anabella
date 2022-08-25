"""Anabella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
#Importamos desde la app esta las views
#LO QUE SE HIZO ACA FUE CREAR LOS PRIMEROS URLS PATTERN (SUS PATH) Y SE LOS CORTO Y PEGÓ EN URLS.PY DEL PROYECTOWEBAPP CREADO, Y LUEGO ENLAZARLOS MEDIANTE EL SEGUNDO PATH CREADO, TENGA UN '' PARA QUE PUEDA TOMAR TODOS LOS PATHS DESDE LA PAGINA HOME, PERO QUE INCLUYA (INCLUDE) LAS URLS DE ESA APP, EN EL QUE VA A TOMAR LA URLS PROYECTOWEBAPP/* EL NOMBRE DE LOS RESTO DE LAS URLS.
# ADEMAS DEBEMOS IMPORTAR, APARTE DE PATH, LA FUNCIÓN INCLUDE ARRIBA.
#ESTE PROCESO SE HACE POR TANTAS APPS TENGA.
#LO UNICO QUE QUEDO FUE EL PATH ADMIN Y EL PATH MENCIONADO LINEA ARRIBA.
#A MEDIDA QUE VOY HACIENDO LOS PATH DE LAS DIFERENTES APP LAS VOY AGREGANDO ACÁ PARA QUE ME DERIVE ALLÍ Y QUE INCLUYA LOS PATH DE ESOS RESPECTIVOS APPS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWebApp.urls')),
    path('servicios/', include('servicios.urls')),
]

