from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass
# 따로 유저를 만들 필요가 없는건지? FK 잘 모르겠음
