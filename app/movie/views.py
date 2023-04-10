"""
Views for the movie APIs.
"""
from django.shortcuts import render
from django.http import HttpResponse
from core.models import Movie
from django.shortcuts import get_object_or_404


def home(request):
    """Retrieve the values submited."""
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html',
                  {'searchTerm': searchTerm, 'movies': movies})


def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')


def signup(request):
    """
    Retrieve the email from the GET request (request.GET.get('email'))
    and send it to signup.html by passing in a key value dictionary,
    {'email': email}
    """
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html',
                  {'movie': movie})
