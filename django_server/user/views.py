from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout
from django.contrib import messages

from .form import get_user, insert_user

# register
class UserRegister(TemplateView):
    """ TemplateView 특징:
        get() 생략 가능 -> 자동 생성
    """
    template_name = 'user/register.html'

    def post(self, request):
        """회원가입 처리"""

        try:
            username = request.POST.get('username').strip()
            password = request.POST.get('password').strip()
            email = request.POST.get('email').strip()

            insert_user(username, password, email)
            return redirect('user-login')

        except ValueError as e:
            messages.error(request, str(e))
            return redirect('user-register')

class UserLogin(View):
    def get(self, request):
        """ View 특징:
            get() 메서드 반드시 구현 
        """
        return render(request, 'user/login.html')
    
    def post(self, request):
        """로그인 처리"""
        try:
            name = request.POST.get('username').strip()
            password = request.POST.get('password').strip()

            user = get_user(name, password)
            login(request, user)  # 세션에 사용자 정보 저장
            return redirect('select_todolist')  # 로그인 성공 시 todolist로 리다이렉트

        except ValueError as e:
            messages.error(request, str(e))
            return redirect('user-login')


class UserLogout(View):
    """ 화면이 필요 없는 경우 View 상속 """
    def get(self, request):
        """로그아웃 처리"""
        logout(request)  # 세션에서 사용자 정보 삭제
        return redirect('user-login')  # 로그아웃 후 로그인 페이지로 리다이렉트