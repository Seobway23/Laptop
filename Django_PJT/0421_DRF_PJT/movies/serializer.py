from rest_framework import serializers
from .models import Actor, Movie, Review
from collections import OrderedDict as OD

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields= '__all__'

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('title',)

#1번째 방법
class MovietitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']

class ActorsDetailSerializer(serializers.ModelSerializer):
    movies = MovietitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields= ['id','movies', 'name']
        read_only_fields = ('movie_set',)
    



class ActorsDetailSerializer(serializers.ModelSerializer):
    movies = MoviesSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields= ['id','movies', 'name']    
    # 
    def to_representation(self, instance):
        represestation = super().to_representation(instance)
        represestation['movies'] = \
            [OD({'title' : od['title']}) for od in represestation['movies']]
        return represestation

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'