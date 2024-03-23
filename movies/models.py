from django.db import models

# Create your models here. How this works:
# 1. Create a class that inherits from models.Model.
# 2. Each class attribute represents a database field.
# 3. Each field is represented by an instance of a field class.
# 4. Each field class has a number of arguments that can be passed to it.
# 5. Each field class has a number of attributes that can be set.
# 6. Each field class has a number of methods that can be called.

# After modifying the models.py file, you need to run the following commands:
# python manage.py makemigrations # this command creates a migration file
# python manage.py migrate # this command applies the migration file to the database

class Movie(models.Model):
    # create attributes for the Movie class
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    actors = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.director}"