from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()