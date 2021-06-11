from django import urls
from django.urls import path
from .views import inicio,nosotros,perros,gatos,formulario

urlpatterns = [

    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('perros/', perros, name="perros"),
    path('gatos/', gatos, name="gatos"),
    path('formulario/', formulario, name="formulario"),
  

]