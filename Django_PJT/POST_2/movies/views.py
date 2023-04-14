from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comments.all()
    context = {
        'movie': movie,
        'comment_form' : comment_form,
        'comments':comments,
    }
    return render(request, 'movies/detail.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=pk)
        print('movie:', movie)
        print(request.POST)
        comment_form = CommentForm(request.POST)
        print('comment_form:', comment_form)
        if comment_form.is_valid():
            print(11111)
            comment = comment_form.save(commit=False)
            comment.movie= movie
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, movie_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)

def likes(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')

def comment_comment_create(request, movie_pk, comment_pk):
    print('hello')
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        comment = Comment.objects.get(pk=comment_pk)
        comment_comment_form = CommentForm(request.POST)
        if comment_comment_form.is_valid():
            comment_comment = comment_comment_form.save(commit=False)
            comment_comment.movie = movie
            comment_comment.user = request.user
            comment_comment.comment = comment
            comment_comment.save()

    return redirect('accounts:login')


def comment_comment_delete():
    return