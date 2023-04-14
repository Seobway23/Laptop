from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    #커스텀을 위해서 model get_user_model로 넣어야 하는데, 여기서 Meta 이너 클래스에서 바꾼다.
    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustionUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name',]

# 두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀해야 함

# User = get_user_model()
# class SignupForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User