from django.urls import path, include
from django.contrib import admin
from . import views #Aca en lugar del punto estaba "ProyectoWebbApp", pero es mejor poner el . para que diga que importe de todos los lugares

from django.conf.urls.static import static

urlpatterns = [

    path('', views.contacto, name="Contacto"),

]