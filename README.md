# Pasos a seguir para inicializar la página web:

## Iniciar una terminal de Bash e instalar virtualenv:

py -m venv venv

## Iniciar virtualenv:

. venv/Scripts/activate

## Crear superuser:

py manage.py createsuperuser

## Instalar django con el siguiente comando:

pip install django

## Generar la base de datos:

py manage.py migrate

## Inicializar el servidor:

py manage.py runserver 

- Página principal, link a páginas secundarias