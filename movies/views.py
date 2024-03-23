from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie


def movies(request):
    movie_list = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movie_list})


def home(request):
    return HttpResponse('Welcome to the Movies App Home Page!')


# view for path to movie details page
def detail(request, id):
    movie = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': movie})

# add movie view
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        if title and director and year:
            Movie.objects.create(title=title, director=director, year=year)
            return HttpResponseRedirect('/movies')
    return render(request, 'movies/add_movie.html')

def delete_movie(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return HttpResponse('Movie does not exist')
    else:
        movie.delete()
    return HttpResponseRedirect('/movies')