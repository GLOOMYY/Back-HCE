# Rutas Back-HCE

El proyecto se divide en 3 apps

- Historia
- Seguimientos
- Users

Para enviar filtros se deben usar querys, para crear pacientes se envia la informacion por body

Ademas todas las rutas permiten Metodo OPTIONS para mas informacion sobre los campos requeridos

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

- [Lista Historias](http://127.0.0.1:8000/historia/):
  - Metodo: GET
  - Filtros: paciente
  - Retorna las historias
- [Crear Historias](http://127.0.0.1:8000/historia/create/):
  - Metodo: POST
  - Crea historias

## Seguimientos

#### SeguimientoEspecialidad

- [Lista Seguimiento Especialidad](http://127.0.0.1:8000/seguimiento/especialidad/):
  - Metodo: GET
  - Filtros: id, historia
  - Retorna los Seguimientos de especialidad
- [Crear Seguimiento Especialidad](http://127.0.0.1:8000/seguimiento/especialidad/create):
  - Metodo: POST
  - Crea Seguimientos de especialidad

#### SeguimientoMedicinaGeneral

- [Lista Seguimiento Medicina General](http://127.0.0.1:8000/seguimiento/general/):
  - Metodo: GET
  - Filtros: id, historia
  - Retorna los Seguimientos de medicina general
- [Crear Seguimiento Medicina General](http://127.0.0.1:8000/seguimiento/especialidad/create):
  - Metodo: POST
  - Crea Seguimientos de medicina general

#### SeguimientoEnfermeria

- [Lista Seguimiento Enfermeria](http://127.0.0.1:8000/seguimiento/enfermeria/):
  - Metodo: GET
  - Filtros: id, historia
  - Retorna los Seguimientos de Enfermeria
- [Crear Seguimiento Enfermeria](http://127.0.0.1:8000/seguimiento/enfermeria/create):
  - Metodo: POST
  - Crea Seguimientos de Enfermeria

#### Estrategias

- [Lista Estrategias](http://127.0.0.1:8000/seguimiento/estrategias/):
  - Metodo: GET
  - Filtros: id, seguimiento_especialidad
  - Retorna las estrategias
- [Crear Estrategias](http://127.0.0.1:8000/seguimiento/estrategias/create):
  - Metodo: POST
  - Crea estrategias

#### Formulario

- [Lista Formularios](http://127.0.0.1:8000/seguimiento/formulario/):

  - Metodo: GET
  - Filtros: id, profesional, paciente, seguimiento_especialidad, seguimiento_medicina_general, seguimiento_enfermeria
  - Retorna los formularios

- [Crear Formulario](http://127.0.0.1:8000/seguimiento/formulario/create):
  - Metodo: POST
  - Crea formularios

#### SignosVitales

- [Lista SignosVitales](http://127.0.0.1:8000/seguimiento/signos-vitales/):

  - Metodo: GET
  - Filtros: id, formulario
  - Retorna los signos vitales

- [Crear SignosVitales](http://127.0.0.1:8000/seguimiento/signos-vitales/create):
  - Metodo: POST
  - Crea signos vitales

#### DatosAntropometricos

- [Lista DatosAntropometricos](http://127.0.0.1:8000/seguimiento/datos-antropometricos/):

  - Metodo: GET
  - Filtros: id, formulario
  - Retorna los datos antropometricos

- [Crear DatosAntropometricos](http://127.0.0.1:8000/seguimiento/datos-antropometricos/create):
  - Metodo: POST
  - Crea datos antropometricos

#### Observaciones

- [Lista Observaciones](http://127.0.0.1:8000/seguimiento/observaciones/):

  - Metodo: GET
  - Filtros: id, formulario
  - Retorna las observaciones

- [Crear Observaciones](http://127.0.0.1:8000/seguimiento/datos-antropometricos/create):
  - Metodo: POST
  - Crea observaciones

#### NotasAclaratorias

- [Lista NotasAclaratorias](http://127.0.0.1:8000/seguimiento/notas-aclaratorias/):

  - Metodo: GET
  - Filtros: id, especialidad, formulario, profesional, historia
  - Retorna las notas aclaratorias

- [Crear NotasAclaratorias](http://127.0.0.1:8000/seguimiento/datos-antropometricos/create):
  - Metodo: POST
  - Crea notas aclaratorias
