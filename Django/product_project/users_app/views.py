from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import User
from .forms import CustomUserCreationForm
from .forms2 import UserForm

# Create your views here.
# 로그인
def sign_in(request):
    if request.method == 'POST':
        # 입력한 폼을 로그인 양식으로 변환
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 해당 로그인 양식으로 로그인 시도
            login(request, form.get_user())
            return redirect('/')
    else:
        # 첫 화면에서는 빈 폼을 보여주기
        form = AuthenticationForm()
    return render(request, "users_app/login.html", {'form':form})

# 로그아웃
def sign_out(request):
    logout(request)
    return redirect('/')

# 회원가입
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/users/sign_in/') # 회원가입 후 로그인 화면으로 이동
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/sign_up.html', {'form':form})

def sign_up2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_address = request.POST['user_address']

        # 기본값 저장
        user = User.objects.create_user(username, email, password)

        # 나머지는 따로 저장
        user.user_name = user_name
        user.user_phone = user_phone
        user.user_address = user_address

        user.save()

        return redirect('/users/sign_in')
    else:
        form = UserForm()
    
    return render(request, 'users_app/sign_up2.html')