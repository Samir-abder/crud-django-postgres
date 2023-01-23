# CRUD con Django y Postgres 🤠🐘

Este es un CRUD que creé con Django y Postgres.
Creada para el tutorial de CRUD con Django y Postgres en mi canal de Youtube.
**Mira el video haciendo click [aquí.](https://youtu.be/sYaEoNy5OGs)** 👈

## Uso
Solo tienes que descargar el código, crear un entorno virtual e instalar las dependencias necesarias. Todo esto con los siguientes comandos:

```
- virtualenv venv
- source venv/bin/activate
- pip install django
- pip install psycopg2
```

Después de eso debes de configurar la base de datos en settings.py para que Django use tu base de datos de PostgreSQL.

```
DATABASES = {
    # PostgreSQL connection database 🐘
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todos_db',
        'USER': 'postgres',
        'PASSWORD': 'YourPassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Tendrás que crear una nueva base de datos llamada 'todos_db' y añadir tu contraseña de PostgreSQL en el settings.py.

Y finalmente correr el servidor:

```
- python3 manage.py runserver
```

Sientete libre de descargar el código y modificarlo a tu antojo. Si tienes alguna duda o sugerencia, no dudes en dejar un comentario en el video. 😉

## Mis Redes Sociales
<a href="https://www.linkedin.com/in/salmeron-alvarado/"><img align="left" src="https://raw.githubusercontent.com/yushi1007/yushi1007/main/images/linkedin.svg" alt="Salmeron | LinkedIn" width="24px"/></a>