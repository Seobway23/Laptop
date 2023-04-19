from django.urls import path
# path는 장고닷 유알엘즈에 있음, path -> 결국 클릭 -> url 이동
from . import views

urlpatterns = [
    path('html/', views.article_html),
]
