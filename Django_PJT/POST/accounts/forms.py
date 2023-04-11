#accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields= ['username', 'email', 'first_name', 'last_name',] #list, tuple 노상관

# 두 form 모두 class Meta: model = User가 등록된 form이기 때문에 반드시 커스텀해야 함
