# Start project
1. 가상 환경 설치
```
python -m venv venv
```

2. django app
- startproject 
```
django-admin startproject pjt(원하는 pjt이름) .
.은 현재 폴더에 생성
```

- startapp
```
python manage.py startapp accounts(원하는 app이름)
```

#  Accounts
1. add App
- settings.py 에서 INSTALLED_APPS에 accounts 추가
```
INSTALLED_APPS = [
    # django Apps
    'accounts',
    ...
]
```

2. rest_framework
- rest_framework란?


  RESTful API의 개발을 단순화하는 일련의 도구 및 기능을 제공하여 직렬화, 인증 및 URL 라우팅과 같은 일반적인 작업을 보다 쉽게 ​​처리할 수 있음


- rest_framework 설치
  
```
pip install rest_framework

```
- add rest_framework
```
INSTALLED_APPS = [
    # rest_framework
    'rest_framework',
    ...
]
```

3. dj-rest-auth
- 회원가입, 인증, 비밀번호 재설정,  사용자 세부 정보 검색, 회원 정보 수정 등 rest API end point 제공

- 패키지 설치
```
pip install 'dj-rest-auth[with_social]'
```

- 앱 등록
```
INSTALLED_APPS = [
    'rest_framework.authtoken',
    ...,
    'dj_rest_auth'

*추가로 registration 해야 함

REST_AUTH = {
  'SESSION_LOGIN': False
}

SITE_ID = 1

...
]

```

- url 등록
```
urlpatterns = [
  path('dj-rest-auth/(원하는 URL)', include('dj_rest_auth.urls)),
]
```

- migrate
```
$ python manage.py makemigrations
$ python manage.py migrate

```


- rest_framework -> token check
![password_token](456456456.png)

- Password Change 
``` 
INSTALLED_APPS = [
    ... ]

REST_FRAMEWORK ={
  # Authentication
  'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
  ]
}
```

- Permission setting
```
DEFAULT_PERMISSION_CLASSES : [
  #permission
  'rest_framework.permissions.AllowAny',
]
```

- article list review
```
from rest_framework.decorators import permission_classes

# decorators를 이용해 authenticated 권한 부여
@permission_classes([IsAuthenticated])
if request.method == 'GET':
  ...
```
