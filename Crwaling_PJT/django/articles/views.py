from django.shortcuts import render
from .models import Article
#json_1
from django.http.response import JsonResponse, HttpResponse

#json_2
from django.core import serializers

#json_3
from .serializers import ArticleSerializer
from rest_framework.response import Response

#DRF에서 api_view데코레이터 작성은 필수
from rest_framework.decorators import api_view

# POST
from rest_framework import status

#Detail
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
@api_view(['GET', 'POST'])
def articles_list(request):
    if request.method =='GET':
        articles = Article.objects.all()
        #many True를 해야 복수형 선택 가능
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        #유효하지 않은 데이터 예외 발생
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    #get 조회만 할 때
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        serializer = ArticleSerializer(article)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




def articles_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
            'number': article.pk,
            'name':article.name,
            'title':article.title,
            'content': article.content,
            }
        )
    return JsonResponse(articles_json, safe=False)

def articles_json_2(reuqest):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


@api_view()
def articles_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


 