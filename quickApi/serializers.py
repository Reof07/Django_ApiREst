''' Serializar.py
    este archivo vincula el modelo Hero con su serializador
    y como debe serializar los datos (como se deben presentar los datos).
'''
# Importamos el modelo que vamos a serializar
from .models import Hero

# Importamos el serializador
from rest_framework import serializers 

class Hero_Serializer(serializers.HyperlinkedModelSerializer):
    ''' Esta clase vincula el modelo 
        con su serializador
    '''

    class Meta:
        model = Hero # Modelo a serializar
        fields = ('id','name', 'alias') # Campos del modelo a serializar