# Django Demo App: Movie Database

This is demo Django App. 

Reference: https://www.youtube.com/watch?v=EuBQU_miReM

## Commands Used:

- django-admin --help
- django-admin startproject movies .
- python manage.py runserver
- python manage.py migrate
- python manage.py createsuperuser

- create movies/views.py
- create movies/models.py
- add Movie class to models.py

- python manage.py makemigrations movies # this creates the model in the database
    Migrations for 'movies':
    movies\migrations\0001_initial.py
        - Create model Movie

- python manage.py sqlmigrate movies 001 # view the sql statement planned
- python manage.py migrate # apply the change
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, movies, sessions
    Running migrations:
    Applying movies.0001_initial... OK

- create movies/admin.py # specify the tables to display on the admin page

- add movie
- delete movie



