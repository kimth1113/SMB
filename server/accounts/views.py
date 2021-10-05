from django.shortcuts import get_object_or_404
from requests.models import get_cookie_header
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import User, UserSerializer,LikeSerializer
from movies.models import Like

User = get_user_model()

@api_view(['POST'])
def signup(request):
    print(request.data)
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')

    if password != password_confirmation:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()    
        user.set_password(request.data.get('password'))
        user.save()
        return Response(data=serializer.data, 
                        status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data['name']
    user = get_object_or_404(get_user_model(), username=username)
    serializer = UserSerializer(user)
    return Response(data=serializer.data)

def following(request, person_id):
    person_user = get_object_or_404(User, pk=person_id)
    request_user = request.user

    if person_user == request_user:
        return Response(status=status.HTTP_404_BAD_REQUEST)
    
    if request_user not in person_user.followings.all():
        person_user.followings.add(request_user)
        # (아래) 새로 추가되어 변경된 팔로잉 정보를 다시 뷰로 보내주기 위한 코드
        serializer = UserSerializer(data=request.data)
        return Response(data=serializer.data)
    else:
        profile_user.followings.remove(request_user)
        # (아래) 기존 팔로잉이 삭제되어 변경된 팔로잉 정보를 다시 뷰로 보내주기 위한 코드
        serializer = UserSerializer(data=request.data)
        return Response(data=serializer.data)
    
@api_view(['DELETE'])
def delete(request):
    password = request.data['password']

    if request.user.password == password:
        request.user.delete()
        return Response(status=status.HTTP_200_OK)
        
    return Response(status=status.HTTP_404_BAD_REQUEST)


@api_view(['POST'])
def change_password(request):
    now_password = request.data['password']
    new_password = request.data['new_password']

    if now_password == request.user.password:
        if now_password != new_password:
            request.user.password = new_password
            return Response(status=status.HTTP_200_OK)
        
    return Response(status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET'])
def mypage(request, user_id):
    user = get_object_or_404(get_user_model(), pk= user_id)
    
    serializer = UserSerializer(user)
    return Response(data=serializer.data)
