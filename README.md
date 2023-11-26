# Back HCE

Backend para el proyecto de Historia Clinica de la materia Ingenieria de Software

## Características

- Permite el manejo de la Historia Clinica de pacientes para incluir nuevos formularios y ver los ya añadidos

## Tecnologías Utilizadas

- Django
- Djangorestframework
- Django-filter
- SQLite

## Requisitos Previos

- asgiref==3.7.2
- Django==4.2.7
- django-filter==23.4
- djangorestframework==3.14.0
- pytz==2023.3.post1
- sqlparse==0.4.4

## Instalación

1. Clona el repositorio: `git clone https://github.com/GLOOMYY/Back-HCE.git`
2. Entra al directorio del proyecto: `cd Back-HCE`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Configura las variables de entorno (Por ahora no se usan).
5. Realiza las migraciones: `python manage.py migrate`
6. Inicia el servidor: `python manage.py runserver`

## Contribuir

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu contribución: `git checkout -b mi-contribucion`
3. Realiza los cambios y haz commit: `git commit -m "Descripción de los cambios"`
4. Haz push a tu rama: `git push origin mi-contribucion`
5. Abre un pull request en GitHub.
