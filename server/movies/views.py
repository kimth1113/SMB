from django.shortcuts import get_object_or_404
from requests.api import get
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .serializers import MovieSerializer, LikeSerializer,ReviewSerializer, MovieCntSerializer
from .models import Movie, Genre, Like, Review, MovieCnt
from django.http import JsonResponse
import requests
import random
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import Count

# 홈페이지: 영화 전체 리스트
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


# 영화 상세조회
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, movie_id=movie_pk)
        movie.count += 1
        movie.save()
        print('#####################', movie.count)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 영화 좋아요 기능
@api_view(['POST'])
def movie_like(request):

    movie_id = str(request.data.get('movie_id'))
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    user_likes = user.like_set.all()
    flag = 1
    for user_like in user_likes:
        if (user_like.movie_id == movie_id):
            user_like.delete()
            flag = 0
    if (flag):
        Like.objects.create(
            user = user,
            movie_id=movie_id
        )


    user_likes = user.like_set.all()
    serializer = LikeSerializer(user_likes, many=True)
    return Response(data=serializer.data)
    
    # if Like.like_users.filter(pk=user.id).exists():
    #     movie.like_users.remove(user)
    #     serializer = MovieSerializer(movie)
    #     return Response(data=serializer.data)
    # else:
    #     movie.like_users.add(user)
    #     serializer = MovieSerializer(movie)
    #     return Response(data=serializer.data)

@api_view(['GET'])
def get_user_likes(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    likes = user.like_set.all()
    serializer = LikeSerializer(likes, many=True)
    return Response(data=serializer.data)


# 영화 장르 확인을 위한 테스트 코드
def movie_genre(request, movie_genre):
    genre = Genre.objects.filter(genre_id=movie_genre)
    print(genre[0].name)


# 영화 추천 알고리즘
@api_view(['GET'])
def movie_reccommendation(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        N = len(movies)
        count_rank = movies[:]

        for i in range(N-1, 0, -1):
            # arr[j]와 그 다음 값을 비교할 거야
            for j in range(i):
                if count_rank[j].count < count_rank[j+1].count:
                    count_rank[j], count_rank[j+1] = count_rank[j+1], count_rank[j]
        
        top_movies = count_rank[0:20]
        
        # num = random.randint(1,100)
        # movie = get_object_or_404(Movie, pk=num)
        serializer = MovieSerializer(top_movies, many=True)
        return Response(serializer.data)


# 검색 기능: 영화 제목 
@api_view(['GET'])
def search(request, movie_title):
    movies = Movie.objects.filter(title__contains=movie_title)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 DB 생성 명령 (100개)
def movie_list(request):
    api_key = '149448f6e724f29673f8ce8767dd1425'

    for page in range(1, 6):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page={page}'
        GEN = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=ko-KR'
        response = requests.get(URL)
        result = response.json()
        G_response = requests.get(GEN)
        G_result = G_response.json()

        for i in range(20):
            if 'release_date' in result['results'][i]:
                Movie.objects.create(
                    adult = result['results'][i]['adult'],
                    genre = result['results'][i]['genre_ids'],
                    movie_id = result['results'][i]['id'],
                    original_title = result['results'][i]['original_title'],
                    overview = result['results'][i]['overview'],
                    poster_path = result['results'][i]['poster_path'],
                    release_date = result['results'][i]['release_date'],
                    title = result['results'][i]['title'],
                    vote_average = result['results'][i]['vote_average'],
                    vote_count = result['results'][i]['vote_count'],
                    count = '0'
                )


# 새로운 영화정보 생성 (admin 계정으로 로그인 시)
# @api_view(['POST'])
# def admin(request):
#     print(request.user)
#     if request.user == admin:
#         # like_users(좋아요)와 count(조회수) 제외
#         Movie.objects.create(
#             adult = request.data['adult'],         
#             genre = request.data['genre'],        
#             movie_id = request.data['movie_id'],
#             original_title = request.data['original_title'],
#             overview = request.data['overview'],
#             poster_path = request.data['poster_path'],
#             release_date = request.data['release_date'],
#             title = request.data['title'],
#             vote_average = request.data['vote_average'],
#             vote_count = request.data['vote_count']  
#         )


# (admin 권한으로) 영화 수정 및 삭제
# @api_view(['PUT', 'DELETE'])
# def admin_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)

#     if request.method == 'PUT':
#         serializer = MovieSerializer(data=request.data, instance=movie)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# 영화 리뷰 조회 및 생성
@api_view(['GET', 'POST'])
def review(request):
    user = get_object_or_404(get_user_model(), pk=request.data['user_id'])

    if request.method == 'GET':
        reviews = user.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)

            reviews = Review.objects.filter(movie_id=request.data.get('movie_id'))
            reviews=reviews.order_by('-pk')
            serializer = ReviewSerializer(reviews, many=True)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


# 영화 리뷰 수정 및 삭제
@api_view(['PUT', 'DELETE'])
def review_detail(request, user_id, review_id):
    User = get_user_model()
    now_user = get_object_or_404(User, pk=user_id)
    review = now_user.review_set.filter(id=review_id)

    if request.user == now_user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(data=request.data, instance=review)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)

        elif request.method == 'DELETE':
            review.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def review_list(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id)
    reviews = reviews[::-1]
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)
    
@api_view(['POST'])
def review_delete(request):
    user_id=request.data.get('user_id')
    review_id=request.data.get('review_id')
    review = get_object_or_404(Review, pk=review_id)

    if (review.user_id != int(user_id)):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    review.delete()
    reviews = Review.objects.filter(movie_id=request.data.get('movie_id'))
    reviews = reviews[::-1]
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

    
@api_view(['GET','POST'])
def movie_cnt(request):
    if request.method == 'GET':
        recommends =MovieCnt.objects.order_by('-cnt')
        recommends = recommends[0:7]
        serializer = MovieCntSerializer(recommends, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        movie_id = str(request.data.get('movie_id'))
        mc_id = 0
        recommends = MovieCnt.objects.all()
        for i in range(len(recommends)):
            if (movie_id==recommends[i].movie_id):
                mc_id = recommends[i].id

        if (mc_id > 0):
            recommend  = get_object_or_404(MovieCnt, pk=mc_id)
            recommend.cnt += 1
            recommend.save()
        else:
            MovieCnt.objects.create(movie_id =movie_id)
        return Response(status=status.HTTP_200_OK)
        


@api_view(['GET'])
def many_rate(request):
    reviews = Review.objects.values('movie_id').annotate(Count('movie_id')).order_by('-movie_id__count')
    reviews = reviews[0:7]
    return Response(data=reviews)
    

@api_view(['GET'])
def movie_manylike(request):
    likes = Like.objects.values('movie_id').annotate(Count('movie_id')).order_by('-movie_id__count')
    likes = likes[0:7]
    return Response(data=likes)

@api_view(['POST'])
def user_reviews(request):
    user_id=request.data.get('user_id')
    reviews =Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def review_update(request):
    user_id=request.data.get('user_id')
    review_id=request.data.get('review_id')
    review = get_object_or_404(Review, pk=review_id)
    print(request.data)
    if (review.user_id != int(user_id)):
        return Response(status=status.HTTP_400_BAD_REQUEST)
  
    serializer = ReviewSerializer(data=request.data, instance=review)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        reviews = Review.objects.filter(movie_id=request.data.get('movie_id'))
        reviews = reviews[::-1]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)


