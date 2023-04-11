from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html',)


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