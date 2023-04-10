from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

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
