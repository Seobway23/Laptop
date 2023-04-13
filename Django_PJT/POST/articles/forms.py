from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        #fields = '__all__'
        exclude = ('user', 'id_like_users',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =('article','user',)
        #fields = '__all__'