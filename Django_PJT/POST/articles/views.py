from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

#인덱스
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html',context)

# 게시글 생성
@login_required
@require_http_methods(['GET', 'POST'])
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
    comment_form = CommentForm()
    comments = article.comments.all()
    context= {
        'article' : article,
        'comment_form':comment_form,
        'comments': comments,
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
    
@require_POST
#게시글 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        # article 객체는 어떻게 저장?
        #comment_form.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')

# 왜 어쩔땐 되고 어쩔때는 안되는 거죠?
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:     
        article = Article.objects.get(pk=article_pk)
        
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
