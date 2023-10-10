from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃 : 로그인유저 -> 로그아웃 / 비로그인 유저 -> x


@login_required  # 로그인이 되어 있지 않다면 로그인 페이지로 이동하게끔 해주는 데코레이터..
def logout(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == "POST":
        # 폼에 대한 유효성 검사
        # 유저 인스턴스 생성
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:  # 'GET'
        # 회원가입 폼을 렌더 보여주기
        form = CustomUserCreationForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 회원탈퇴
    # user = request.user
    # user.delete()
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    # 회원수정 폼 -> 로직
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:  # 'GET'
        # 회원수정 폼이 보이게..
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request):
    if request.method == "POST":
        # 비밀번호를 변경처리 로직
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()  # 유저 업데이트(저장)
            # 변경된 유저 정보를 가지고 세션을 변경하게 처리...
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:  # 'GET"
        # 비밀번호 변경 폼
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
