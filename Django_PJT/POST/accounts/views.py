from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model

#login views
def login(request):
    #만약 request가 POST라면
    if request.method == 'POST': 
        # 포스트 요청인 AuthenticationForm을 form에 담고 
        form = AuthenticationForm(request, request.POST)
        # 만약 유효하다면, 
        if form.is_valid():
            # auth_login이 뭐지 ?
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    else:
        form = AuthenticationForm()
    
    context = {'form' : form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    print(1)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #UserCreationForm의 save 메서드는 user를 반환
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    # 탈퇴 후, 로그아웃
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form':form,
        }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)

