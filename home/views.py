from django.shortcuts import render
from movies.models import Movie  # Import the actual Movie model

def index(request):
    movies = Movie.objects.all()  # Get real movies from database
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html', {'template_data': template_data})

def about(request):
    template_data = {
        'title': 'Movies Store - About Us'
    }
    return render(request, 'home/about.html', {'template_data': template_data})