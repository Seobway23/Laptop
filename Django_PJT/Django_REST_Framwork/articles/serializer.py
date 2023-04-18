from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        #read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    #comment_set = CommentSerializer(many=True, read_only = True)
    # comments = CommentSerializer(many=True, read_only = True)
    # comments를 쓰려면, related_name 을 바꾼값을 적용해야 함, default값이 comment_set임
    class Meta:
        model = Article
        fields = '__all__'
