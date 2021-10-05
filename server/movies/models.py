from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, 
    #                                     related_name="like_movies",
    #                                    through="Like")
    adult = models.BooleanField()
    genre = models.TextField()
    movie_id = models.IntegerField()
    original_title = models.CharField(max_length=1000)
    overview = models.TextField()
    poster_path = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=1000)
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    count = models.IntegerField(blank=True)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.TextField()
    rate = models.TextField()
    username = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.TextField()
    
class Genre(models.Model):
    genre_id = models.TextField()
    name = models.TextField()

class MovieCnt(models.Model):
    movie_id = models.TextField()
    cnt = models.IntegerField(default=1)