from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('<int:pk>/<int:comment_pk>/comments/', views.comment_comment_create, name='comment_comment_create'),
    path('<int:pk>/<int:comment_pk>/<int:comment_comment_pk>/delete', views.comment_comment_delete, name='comment_comment_delete'),
]
