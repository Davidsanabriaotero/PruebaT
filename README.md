# Proyecto Prueba Tecnica

Para realizar la correcta instalación y configuración del aplicativo se deben seguir los siguientes pasos.

## Instalación y Configuración

1. Crear una base de datos en postgreSQL
2. Verificar que tiene instalada la biblioteca "psycopg2" de no ser asi puede ser instalada desde la terminal con el siguiente codigo `pip install psycopg2`
3. Modificar en  el archivo settings.py que se encuentra en la carpeta pruebaT la configuración de la base de datos teniendo en cuenta los parametros utilizados para configurar la base de datos creada en postgreSQL.

   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_database',
           'USER': 'nombre_usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
4. Instalar Django Rest Framework, esto se puede realizar con el siguiente comando desde la terminal `pip install djangorestframework`
5. Ejecute el comando `python manage.py makemigrations` para generar los archivos de migración para la base de datos PostgreSQL.
6. Ejecute el comando `python manage.py migrate` para aplicar las migraciones y crear las tablas en la base de datos PostgreSQL.
7. Cree un super usuario para ingresar al sistema, para esto se debe ejecutar el siguiente comando: `python manage.py createsuperuser`
8. para cargar los eventos de ejemplo iniciales, debe dirigirse a la ruta de la raiz del proyecto y en la terminal escribir el siguiente comando `python .\manage.py loaddata .\eventos_de_ejemplo.json`
9. Ejecute el comando `python manage.py runserver` para iniciar el servidor de desarrollo de Django.
10. ingrese a `http://127.0.0.1:8000/admin/`  eh inicie sesión para poder usar las funcionalidades de la API.

## Uso de las funcionalidades de la API

Para utilizar las funcionalidades de la API se puede hacer uso de la vista por defecto de DRF, para acceder a ella se debe abrir el navegador y escribir: `http://127.0.0.1:8000/api/`

    1. para gestionar los eventos se debe acceder a la url:`http://127.0.0.1:8000/api/eventos/` desde el navegador o desde aplicaciones como postman alli se podran realizar las siguientes peticiones:
        * crear evento: `http://127.0.0.1:8000/api/eventos/`  método POST
        * obtener todos los eventos: `http://127.0.0.1:8000/api/eventos/`  método GET
        * obtener un evento: `http://127.0.0.1:8000/api/eventos/<idEvento>/`  método GET
        * actualizar un evento: `http://127.0.0.1:8000/api/eventos/<idEvento>/` método PUT
        * eliminar un evento (Soft Delete): `http://127.0.0.1:8000/api/eventos/<idEvento>/` método DELETE
        * cambiar estado del evento a revisado: `http://127.0.0.1:8000/api/eventos/<idEvento>/cambiar_estado/` método GET
        * obtener los eventos que requieren gestión: `http://127.0.0.1:8000/api/eventos_Requieren_Gestion/` método GET
        * obtener los eventos que no requieren gestión(sin Gestion): `http://127.0.0.1:8000/api/eventos_Sin_Gestion/` método GET

    2. para revisar  los logs de los eventos se debe acceder a la url:`http://127.0.0.1:8000/api/logeventos/` desde el navegador o desde aplicaciones como postman alli se podran revisar todos los logs relacionados.
