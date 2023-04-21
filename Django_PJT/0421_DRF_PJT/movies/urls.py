from django.urls import path
from . import views

urlpatterns = [
    path('actor_list/', views.actor_list),
    path('actor_list/<int:actor_pk>/', views.actor_detail),

    path('movie_list/', views.movie_list),
    path('movie_list/<int:movie_pk>/', views.movie_detail),
    path('movie_list/<int:movie_pk>/reviews/', views.create_review),

    path('review_list/', views.review_list),
    path('review_list/<int:review_pk>/', views.review_detail),

    



]