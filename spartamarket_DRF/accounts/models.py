from django.db import models
from django.contrib.auth.models import AbstractUser

#username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력
#장고 기본 제공 : username, 비밀번호, 이름(first,last), 이메일
#추가 모델은 : 닉네임, 생일
#이메일, 이름
class User(AbstractUser):
    name = models.CharField(max_length=10)
    email =  models.EmailField()
    nickname = models.CharField(max_length=20)
    birthday = models.DateField()
