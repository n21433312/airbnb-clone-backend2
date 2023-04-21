import jwt
import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from . import serializers, models

class Me(APIView):
     
    permission_classes = [IsAuthenticated]

    def get(self, requset):
        user = requset.user
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
     
    def put(self, request):
        user = request.user
        serializer = serializers.PrivateUserSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class Users(APIView):
    
    def post(self,request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class PublicUser(APIView):

    def get(self, requset, username):
        try:    
            user = models.User.objects.get(username=username)
        except models.User.DoesNotExist:
            raise NotFound
        serializer = serializers.PrivateUserSerializer(user)
        return Response(serializer.data)
    

class ChangePassword(APIView):

    
    permission_classes = [IsAuthenticated]

    def put(self, requset):
        user = requset.user
        old_password = requset.data.get("old_password")
        new_password = requset.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError
        if user.check_password(old_password):
            user.set_password(new_password) #set_password는 new_password를 해쉬할 때만 작동한다, 따라서 uesr.save()가 필요
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class LogIn(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username = username,
            password = password,
        )
        if user:
            login(request, user)
            return Response({"Ok":"Welcome!"})
        else:
            return Response({"error": "wrong password"})
        

class LogOut(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, requset):
        logout(requset)
        return Response({"Ok":"Bye"})


class JWTLogIn(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(
            request,
            username = username,
            password = password,

        )
        if user:
            token = jwt.encode({"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256", )
            return Response({"token": token})
        else:
            return Response({"error":"wrong password"})
        
class GithubLogIn(APIView):

    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post(
                f"https://github.com/login/oauth/access_token?code={code}&client_id=bb92679c65bc26a33c95&client_secret={settings.GH_SECRET}",
                                        headers={
                                            "Accept": "application/json"},
                                        )
            access_token = access_token.json().get("access_token")
            user_data = requests.get("https://api.github.com/user", 
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_data = user_data.json()
            user_emails = requests.get("https://api.github.com/user/emails", 
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json",
                },
            )
            user_emails = user_emails.json()
            try:
                user = models.User.objects.get(email=user_emails[0]["email"])
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except models.User.DoesNotExist:
                user = models.User.objects.create(
                    username=user_data.get("login"),
                    email=user_emails[0]["email"],
                    # name=user_data.get("name"), 깃허브 프로필에 name 속성이 없기에 오류가 남
                    avatar=user_data.get("avatar_url"),
                )
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class KakaoLogIn(APIView):
    
    def post(self, request):
        try:
            code = request.data.get("code")
            access_token = requests.post("https://kauth.kakao.com/oauth/token",
                headers = {"Content-Type": "application/x-www-form-urlencoded"},
                data={
                    "grant_type": "authorization_code",
                    "client_id": "7a12da799e8d897b8f936259a2fe6c03",
                    "redirect_uri": "http://chovychovy.xyz/social/kakao",
                    "code" : code,
                },
            )
            access_token = access_token.json().get("access_token")
            user_data = requests.get("https://kapi.kakao.com/v2/user/me",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
                },
            )
            user_data = user_data.json()
            kakao_account = user_data.get("kakao_account")
            profile = kakao_account.get("profile")
            try:
                user = models.User.objects.get(email=kakao_account.get("email"))
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            except models.User.DoesNotExist:
                user = models.User.objects.create(
                    email = kakao_account.get("email"),
                    username = profile.get("nickname"),
                    name = profile.get("nickname"),
                    avatar = profile.get("profile_image_url"), 
                )
                user.set_unusable_password()
                user.save()
                login(request, user)
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

            