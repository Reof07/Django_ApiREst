# Importamos Path e include 
from django.urls import path, include

# Importamos los routes from REST
from rest_framework import routers

# Importamos las views. 
from . import views

# Creamos una instancia routes
router = routers.DefaultRouter()
# 
router.register(r'heroes', views.Hero_ViewSet)

# Conecta el APi Utilizando el enrutador automatico de url.
# Incluimos URl de inicio de sesion para la API navegable.

urlpatterns = [ 
    path('', include (router.urls)), 
    path('api-auth/', include ('rest_framework.urls', namespace = 'rest_framework')) 
]