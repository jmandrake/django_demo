from .models import Movie
from django.contrib import admin


# add the Movie model to the admin site
# Note: the changes made to the admin site will not be visible until the server is restarted
admin.site.register(Movie)