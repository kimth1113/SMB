from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['article']
        
class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['article']
