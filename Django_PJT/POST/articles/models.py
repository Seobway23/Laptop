from django.db import models
from django.conf import settings

# class Article(models.Model):
#     title = models.CharField(max_length=30)
#     content = models.TextField()


class Article(models.Model):
    # user 모델을 참조할 때는 models.py 에서는 settings.AUTH_USER_MODEL
    # 다른 모든 곳에서는 get_user_model()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True) # defualt값 False,  True인 경우 필드 비울 수 있음 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name = 'comments') #article이 삭제되면 comment도 삭제
    # related_name => 역참조되는 네임 바꾸기
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # comment 클래스의 정의한 것 중에서 str인 경우 -> content를 반환한다는 뜻
    def __str__(self):
        return self.content