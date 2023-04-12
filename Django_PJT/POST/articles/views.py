from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.


#인덱스
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html',context)

# 게시글 생성
def create(request):
    if request.method == 'POST':
        print('POST')
        #포스트로 들어오면, 수정하는 거니까 form에 저장해줘
        form = ArticleForm(request.POST, request.FILES) #파일 및 이미지는 request POST가 아닌, FILES로 넘어감
        if form.is_valid(): #유효한지 체크해
            article = form.save(commit=False) #커밋하기 전에 유저 이름 확인해
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)

    elif request.method == 'GET': #사실 elif나 else나 똑같음 POST or GET이기 때문
        print('GET')
        form = ArticleForm()

    context = {'form': form}                                  #context에 담아
    return render(request,'articles/create.html', context)    #creat.html 보여줘

#게시글 디테일
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context= {
        'article' : article,
    }
    return render(request,'articles/detail.html', context)

#게시글 수정
def update(request, pk):
    article = Article.objects.get(pk=pk) # 특정 pk의 딕셔너리 형태의 DB의 키를 orm을 통해 article로 설정-> 만약 이름이 같다면 임의의 난수값을 붙여 저장함
    if request.method =="POST":
        form = ArticleForm(request.POST,request.FILES ,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk=article.pk) #다시 url 요청

    elif request.method == 'GET':
        form = ArticleForm(instance=article)
        context = {'article': article,'form' : form,}                                 
        return render(request,'articles/update.html', context)    
#게시글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method=='POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)