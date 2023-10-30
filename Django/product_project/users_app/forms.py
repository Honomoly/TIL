from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# 회원가입 폼(빌트인)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        # password는 자동 포함이기 때문에 여기다 쓰면 2번 중복되어서 나온다
        fields = ('username', 'email', 'user_name', 'user_phone', 'user_address')
        labels = {
            'username': 'ID',
            'email': '이메일',
            'user_name': '성명',
            'user_phone': '전화번호',
            'user_address': '주소'
        }