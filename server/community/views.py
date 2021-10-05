from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import ArticleSerializer, CommentSerializer, CommentListSerializer
from .models import Article, Comment
from community import serializers
from django.contrib.auth import get_user
import copy
# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.order_by('-pk')
        print(articles)
        serializer = ArticleSerializer(articles, many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
    # POST: 로그인 시에도 안되면 수정 필수
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(data=request.data, instance=article)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data)

@api_view(['POST'])
def article_delete(request, article_id):
    user_id = request.data.get('user_id')
    article = get_object_or_404(Article, pk=article_id)

    if (article.user != user_id):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    article.delete()
    articles = Article.objects.all()
    serializer = CommentListSerializer(articles, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(data=serializer.data)
    # POST: 로그인 시에도 안되면 수정 필수
    elif request.method == 'POST':  
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                    

@api_view(['PUT', 'DELETE'])
def comment_detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_delete(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = article.comment_set.filter(id=comment_id)
    comment.delete()
    comments = article.comment_set.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(data=serializer.data)


@api_view(['POST'])
def article_update(request,article_id ):
    user_id = request.data.get('user')
    article = get_object_or_404(Article, pk=article_id)


    if (str(article.user_id) != user_id):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = ArticleSerializer(data=request.data, instance=article)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data)
