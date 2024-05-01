from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializers import AccountsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model


class AccountListAPIView(APIView):

    def post(self, request):
        # 회원가입하기
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 비밀번호 암호화 처리하기
            data = serializer.data
            id = data.get('id')
            user = get_user_model().objects.get(id=id)# 패스워드를 암호화하는 기능이 get_user_model안에 있다. , 방금 만든 유저 갖고오기
            user.set_password(request.data.get('password'))# 입력한 패스워드를 가져오고, set_password 메소드가 알아서 암호화를 해서 할당해준다
            user.save()  # 조작한 데이터를 DB에 저장
            return Response(data, status=status.HTTP_201_CREATED)
    
    def get(self, request, username):
        user = get_object_or_404(User,username = username) # 한 유저만 가져오기
        serializer = AccountsSerializer(user)
        return Response(serializer.data)