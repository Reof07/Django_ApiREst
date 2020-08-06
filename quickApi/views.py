# Importamos desde REST viewsets
from rest_framework import viewsets

# Importamos el serializador del modelo Hero
from .serializers import Hero_Serializer

# Importamos el modelo Hero.
from .models import Hero

# Create your views here.
class Hero_ViewSet(viewsets.ModelViewSet):
    '''
    '''
    # la clase ModelViewSet de la que podemos heredar
    # y que nos hará todo el trabajo de recuperación y 
    # renderización de la información.
    
    # Obtenemos el queryset desde la base de datos
    # con todos los Heros.
    queryset = Hero.objects.all().order_by('name')

    # Creamos una instancia de Hero_seralizer
    serializer_class = Hero_Serializer