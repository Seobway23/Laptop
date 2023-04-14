from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustionUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login(request):
    # 페이지에서 내요을 적었다면, 
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    
    # 페이지에 들어가지 않았다면, 들어가게 해야지
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render( request, 'accounts/login.html', context )

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.method == 'POST':
        #저장해, 로그인해
        form = CustomUserCreationForm(request.POST)
        #유효하면 저장해
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    
    #페이지에 들어가지 않았다면, 들어가
    else:
        form = CustomUserCreationForm()
    context = {'form': form }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    #탈퇴후 로그아웃
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')

def update(request):
    if request.method=='POST':
        form = CustionUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        
    else:
        form = CustionUserChangeForm(instance=request.user)
        context = {'form':form}
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            #세션 업데이트 후 상태 유지
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {'person': person, }
    return render(request, 'accounts/profile.html', context)

def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
