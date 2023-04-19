from django.db import models

# Create your models here.
class Article(models.Model):
    number = models.IntegerField()
    name = models.TextField()
    title = models.TextField()
    content = models.TextField()


# 모델에서는 models.Model을 쓰는 이유?