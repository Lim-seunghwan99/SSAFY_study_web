from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
from django.contrib.auth import get_user_model

# Create your models here.

# **모델폼** (모델을 기존 장고에 있었던 auth.User 클래스)
# -> 해당 모델을 변경하기 위해서 상속 받아서 커스텀을 해야한다.!!!


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # User # accounts.User


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        password.help_text = "Raw passwords are not stored, so there is no way to see this ""users password, but you can change the password using "'<a href="../change_password/">this form</a>.'

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
