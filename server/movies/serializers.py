from rest_framework import serializers
from .models import Movie, Like, Review, MovieCnt


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['like_users', 'count']


class LikeSerializer(serializers.ModelSerializer):

     class Meta:
         model = Like
         fields = '__all__'
         read_only_fields = ['user']

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']



class MovieCntSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCnt
        fields = "__all__"
