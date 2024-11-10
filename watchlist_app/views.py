from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    """
    This function retrieves a list of movies from the database and renders them in a template.

    Parameters:
    request (HttpRequest): The incoming request object containing information about the client.

    Returns:
    HttpResponse: The rendered template with the list of movies.
    """
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(movie)
    data = {
        "movie": movie.name,
        "description": movie.description,
        "active": movie.active,
    }
    return JsonResponse(data)
