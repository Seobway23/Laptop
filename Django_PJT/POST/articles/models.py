from django.db import models
from django.conf import settings

# class Article(models.Model):
#     title = models.CharField(max_length=30)
#     content = models.TextField()


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True) # defualt값 False,  True인 경우 필드 비울 수 있음 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments') #article이 삭제되면 comment도 삭제
    # related_name => 역참조되는 네임 바꾸기
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content