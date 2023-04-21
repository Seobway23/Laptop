from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Actor, Movie, Review
from .serializer import ActorsSerializer, MoviesSerializer, ReviewsSerializer, ActorsDetailSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# ACTOR
@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorsSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = Actor.objects.get(pk = actor_pk)
    movies = Movie.objects.filter(actors=actor)
    #print(movies)
    #movies = Movie.actors.all(actor_pk)
#    print('actor:', actor)
    serializer = ActorsDetailSerializer(actor)
#    print('serializer:',serializer.data)
    
    return Response(serializer.data)
    

# MOVIE
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    serializer = MoviesSerializer(movie)
    return Response(serializer.data)



# REVIEW
@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk = review_pk)

    if request.method == 'GET':
        serializer = ReviewsSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewsSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewsSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)

    return Response(serializer.data)
