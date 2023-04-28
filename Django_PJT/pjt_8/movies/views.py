from django.shortcuts import render
from django.views.decorators.http import require_safe
from rest_framework.decorators import api_view
from .models import Movie
from rest_framework.response import Response
from .serializer import MovieListSerializer
import random


# Create your views here.
@require_safe
# @api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    # serializer = MovieListSerializer(movies, many=True)
    # return Response(serializer.data)
    context = {
        'movies' : movies
    }    
    return render(request, 'movies/index.html', context)
    #return render( ~~ ,context ={})

# 

@require_safe
@api_view(['GET'])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    #serializer = MovieListSerializer(movie)
    context ={
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)
    

@require_safe
@api_view(['GET'])
def recommended(request):
    movies = Movie.objects.all()
    # serializers = MovieListSerializer(movies, many = True)
    # print(serializers)
    # # for serializer in serializers:
    # #     print(serializer)
    # #     break
    recommended_movies = []
    for movie in movies:
        if movie.vote_count >= 15000:
            recommended_movies.append(movie)
    
    context = {
        'recommended_movies' : recommended_movies[:10]
    }
    return render(request, 'movies/recommended.html', context)