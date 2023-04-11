from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('hello/', views.hello, name='hello'),
    path('catch/', views.catch, name='catch'),
    path('throw/', views.throw, name='throw'),
    path('create/', views.create, name='create'),
]