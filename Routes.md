# Rutas Back-HCE

El proyecto se divide en 3 apps

- Historia
- Seguimientos
- Users

Para enviar filtros se deben usar querys, para crear pacientes se envia la informacion por body

A continuación se pondran las rutas disponibles para cada una de estas apps y sus respectivos metodos

## Users

Esta app se divide en dos principales modelos

#### Profesional de la salud

- [Lista Profesionales](http://127.0.0.1:8000/users/profesional/):
  - Metodo: GET
  - Filtros: especialidad
  - Retorna los profesionales de la salud
- [Crear Profesionales](http://127.0.0.1:8000/users/profesional/create):
  - Metodo: POST
  - Crea profesionales de la salud

#### Paciente

- [Lista Pacientes](http://127.0.0.1:8000/users/paciente/):
  - Metodo: GET
  - Retorna los pacientes
- [Crear Pacientes](http://127.0.0.1:8000/users/paciente/create):
  - Metodo: POST
  - Crea pacientes

## Historia

## Seguimientos
