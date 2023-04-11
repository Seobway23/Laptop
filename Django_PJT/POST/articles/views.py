from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html',context)


def hello(request):
    context = {
        'name': 'aiden'
    }
    return render(request, 'articles/hello.html',context)


def catch(request):
    return render(request, 'articles/catch.html')

def throw(request):
    print(request)
    return

def create(request):
    return render(request, 'articles/create.html')