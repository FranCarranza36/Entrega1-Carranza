# Pasos a seguir para inicializar la página web:

## Iniciar una terminal de Bash e instalar virtualenv:

py -m venv venv

## Iniciar virtualenv:

. venv/Scripts/activate

## Instalar django con el siguiente comando:

pip install django

## Generar la base de datos:

py manage.py migrate

## Crear superuser:

py manage.py createsuperuser

## Inicializar el servidor:

py manage.py runserver 

## Aclaraciones:

- Se muestra por defecto el mensaje que indica que no se han encontrado deportistas según la clase seleccionada. Se considera que si el usuario desea realizar una búsqueda de todos los usuarios debe dejar los 3 campos en blanco sin excepción.
- Solo está permitido el ingreso de valores correctos según el campo. Por ejemplo, no podrán colocarse letras en el campo "Edad" ni números en el campo "Apellido".
- No se permite introducir caracteres especiales, tanto en la búsqueda como en la creación de deportistas (a excepción de letras minúsculas o mayúsculas con acento). Los errores se encuentran especificados y aclarados.
- Todos los campos son obligatorios al cargar un deportista. De no ser así, un mensaje indica que es obligatorio llenar el campo.
- Para crear un deportista primero se accede a la opción de la clase deseada en la parte superior del Home, y luego se ingresa al link "Crear Nuevo X".
- Se permite introducir primer y segundo nombre con espacio, tanto en la búsqueda como en la creación de deportistas.
- Para una ingresar al Panel de Administración de Django, ir a http://127.0.0.1:8000/admin/ o donde corresponda según la IP y puerto del servidor montado.