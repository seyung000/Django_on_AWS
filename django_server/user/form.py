# 로그인 검증

from django.contrib.auth import authenticate
from .models import CustomUser

def insert_user(username:str, password:str, email:str) -> None:
    """회원가입 처리 함수"""
    user = CustomUser.objects.create_user(
        name = username,
        password = password,
        email = email
    )

def get_user(username:str, password:str) -> CustomUser:
    """로그인 검증 함수"""
    if not CustomUser.objects.filter(name=username).exists():
        raise ValueError(f"{username}은 존재하지 않는 사용자명입니다.")
    
    is_user = authenticate(name=username, password=password)

    return is_user