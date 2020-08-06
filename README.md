# Primeros pasos con Django Rest_framework 
django rest_framework es un framework que nos permite crear ApiRest a travez de la serializacion de los modelos django.

## pasos para crear nuestra primera ApiRest

* Configurar django.
* Crear un modelo en la base de datos que admi django ORM.
* Configurar el marco djando rest
* Serializar el paso 2. 
* Crear los puntos finales en urls.py.

### Configurar Django 
Para crear una aplicacion Django debemos instalarlo. Sin embargo es muy facil para eso por buenas practicas es recomendable crear un entorno virtual es nuestro proyecto.

* **python -m venv env** (env es el nombre del ambiente virtual). Una vez creado debomos activarlo. 

#### Instalar Django
Ahora ya podemos instarlar Django y Django Rest_framework en nuestro proyecto: 

**pip install django**
**pip install djangorestframework**

#### Creamos nuestro proyecto principal:

**django-admin startproject (name) .**

#### Creamos nuestra apliacion Api:
Podriamos crear nuestra Api en la estructura de carpeta como esta ahora, sin embargo, la mejor practica es separar su proyecto Django en aplicaciones separadas. 

**python manage.py startapp quickApi**

Ahora necesitamos decirle a django que reconozca la aplicacion que acabamos de crear, entonces nos vamos a quickstart/setting.py y en **INSTALLED_APPS** agregamos nuestra aplicacion **'quickApi'** y **'rest_framework'**.

#### migramos la base de datos

**python manage.py makemigrations**

**python manage.py migrate**

#### Creamos superusuario
**python manage.py createsuperuser**

ahora ya estamos listos para provar nuestra aplicacion y verificar que funciones. 

**python manage.py runserver**

#### Creamos un modelo Hero en nuestra base de datos
Un modelo es una represetacion de la estructura de la base de datos de nuestra app, contiene informacion sobre sus datos.
 
**quickApi/model.py** 

Un modelo es una clase de python que hereda de models.Model esta clase representa el nombre de la tabla en una base de datos mientras que los atributos de clases representan a los campos en la base de datos.

*nota:* Cada vez que realizamos algun cambio en la base de datos debemos realizar nuestras respectivas migraciones.

#### Registrar nuestro modelo Hero en el sitio de administracion.

Para poder agregar nustro modelo al site admin debemos registralo.

path: **quickstart/admi.py**

Import nuestro modelo en el archivo. 
**from .models import Hero**
y luego
**admin.site.register(Hero)**

Entramos al sitio y agregamos algunos datos a nuestra tabla.

# Usado Django REST framework 
Es hora de pensar  en nuestra API de Hero, necesitamos serializar los datos de nuestra base de datos a traves de puntos finales. Ya configuramos nuestro rest_framework a nuestro proyecto.

La estructura basica de DRF se basa en 3 componentes: serializadores, vistas y route. 

* Los route: nos permiten definir cómodamente conjuntos de urls y nos encaminan a nuestros métodos en función del verbo HTTP (GET, POST, PUT, PATCH...).

* Las vistas:  no son más que extensiones de las class-view de django, pero de alguna forma vitaminadas para simplificarnos el enganche con los routers, los serializadores y los modelos y en lugar de renderizar un html como respuesta devolver de forma sencilla un json

* Los serializadores: nos permiten definir al detalle cómo serán las respuestas que devolverá nuestro API y cómo procesaremos el contenido de las peticiones que nos lleguen.

## Serializar el modelo Hero 
Para serializar nuestro modelo Hero necesitamos contarle a Rest sobre nuestro modelo y como debe serializar los datos.

para hacerlo debemos crear un nuevo archivo en **quickApi/serializers.py**  en este archivo pyhton necestiamos_

* importar el modelo Hero
* importar el serializador REST framework
* crear una clase  que vincule al Hero con su serializador. 

Que es el **HyperlinkedModelSerializer** 
 clase es similar a la ModelSerializerclase, excepto que utiliza hipervínculos para representar relaciones, en lugar de claves primarias.

*Para mostrar los datos serializados solo debemos conectar las vistas y las urls.*

#### vistas: 
para renderizar los diferentes Hero en formatos json necesitamos:

* Consultar la DB para todos los heroes 
* Pasamos el queryset que acabamos de solicitar al serializador para convertirlo en json.

#### Routes: 
* El ultimo paso antes de poder ver nuestros datos serializados es asignar una url al conjunto de vistas que acabamos de crear.

En Django, las urls se resuelven primero a nivel del proyecto principal para asignar una url que no lleve hasta nuestro conjunto de vitas debemos ubicar el archivo *urls.py* de mi proyecto raiz.

Una vez en la carpeta solo debemos asignar la url a nuestra APi. usando el metodo *include()*

* Urls Api, como has podido notar hemos incluido una nueva ruta a un archivo que no hemos creado, para eso debemos dirigirnos a nuestra api y crear el archivo *urls.py* alli es donde Django buscara las instrucciones sobre como enrutar estas urls.
