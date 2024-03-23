from django.db import models

# Create your models here. How this works:
# 1. Create a class that inherits from models.Model.
# 2. Each class attribute represents a database field.
# 3. Each field is represented by an instance of a field class.
# 4. Each field class has a number of arguments that can be passed to it.
# 5. Each field class has a number of attributes that can be set.
# 6. Each field class has a number of methods that can be called.
# 7. Each field class has a number of properties that can be accessed.
# 8. Each field class has a number of built-in methods that can be overridden.
# 9. Each field class has a number of built-in properties that can be accessed.
# 10. Each field class has a number of built-in attributes that can be accessed.



class Movie(models.Model):
    # create attributes for the Movie class
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year}) by {self.director}"