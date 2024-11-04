# Hack4U Academy Courses Library

Una biblioteca Python para consultar cursos de la academia Hack4U.

## Cursos disponibles:

- Introccion a Linux [15 Horas]
- Personalizacion de Linux [3 Horas]
- Introduccion al Hacking [53 Horas]
- Python Ofensivo [35 Horas]

## Instalacion

Instala el paquete usando `pip3`:

```python3
pip3 install hack4u-silv
```

## Uso basico

### Listar todos los cursos

```python
from hack4u_silv import list_courses

for course in list_courses:
    print(course)
```

### Obtener un curso por nombre

```python
from hack4u import get_course_by_name

print(get_course_by_name("Python Ofensivo"))
```

### Calcular duracion total de los cursos

```python3
from hack4u_silv.utils import total_duration
print(f"Total: {total_duration()} horas")
```