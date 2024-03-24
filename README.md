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

## Extras
- add description and actors fields to the movies table
- test edit movies using admin UI

## pytest: make sure you're in the venv
- pip install pytest
- pip install pytest-django
- pip install pytest-cov
- create movies/views_test.py and add your tests
- export DJANGO_SETTINGS_MODULE=movies.settings

- pytest (run pytest from the project root)
> $ pytest  
> \=========== test session starts ======================  
> platform win32 -- Python 3.9.0, pytest-8.1.1, pluggy-1.4.0  
> django: version: 4.2.11, settings: movies.settings (from env)  
> rootdir: C:\\projects\\django\\django\_demo  
> plugins: cov-4.1.0, django-4.8.0  
> collected 3 items
> 
> movies\\views\_test.py ... \[100%\]
> 
> \============== 3 passed in 0.17s ====================


- pytest --cov=movies (test coverage report)
> $ pytest --cov=movies  
> \============== test session starts ===================  
> platform win32 -- Python 3.9.0, pytest-8.1.1, pluggy-1.4.0  
> django: version: 4.2.11, settings: movies.settings (from env)  
> rootdir: C:\\projects\\django\\django\_demo  
> plugins: cov-4.1.0, django-4.8.0  
> collected 3 items
> 
> movies\\views\_test.py ... \[100%\]
> 
> \----------- coverage: platform win32, python 3.9.0-final-0 -----------  
> Name Stmts Miss Cover
> 
> ---
> 
> movies\__init.py 0 0 100%_  
> _movies\\admin.py 3 0 100%_  
> _movies\\asgi.py 4 4 0%_  
> _movies\\migrations\\0001\_initial.py 5 0 100%_  
> _movies\\migrations\\0002\_movie\_actors\_movie\_description.py 4 0 100%_  
> _movies\\migrations\_init_.py 0 0 100%  
> movies\\models.py 9 1 89%  
> movies\\settings.py 18 0 100%  
> movies\\urls.py 4 0 100%  
> movies\\views.py 29 12 59%  
> movies\\views\_test.py 21 0 100%  
> movies\\wsgi.py 4 4 0%
> 
> ---
> 
> TOTAL 101 21 79%
> 
> \====================3 passed in 0.27s ==================
