from django.urls import path
# path는 장고닷 유알엘즈에 있음, path -> 결국 클릭 -> url 이동
from . import views

urlpatterns = [
    path('json_1/', views.articles_json_1),
    path('json_2/', views.articles_json_2),
    path('json_3/', views.articles_json_3),
    path('v1/', views.articles_list),
    path('v1/<int:article_pk>/', views.article_detail),
]