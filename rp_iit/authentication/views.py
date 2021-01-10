from decouple import config
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserCreateAndLoginSerializer as UserSerializer

api_key = config('api_key')

class UserRegisterView(generics.GenericAPIView):
    """
    Register and Login API
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            db_user = User.objects.filter(phone=request.data['phone'])
            if not db_user:
                #TODO:
                # 1)encrypt session key
                # 2)review session key storege
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(is_verified=True)
                    user = User.objects.filter(id=serializer.data['id'])
                    if user.exists():
                        login(request,user[0])
                        return Response((user[0].id),status= status.HTTP_201_CREATED)
                    else:return Response({"detail":"user not exists"})
                return Response({'detail':serializer.errors})
            else:
                if db_user[0].is_verified:
                    db_user[0].session_key = request.data['session_key']
                    db_user[0].save()
                    login(request,db_user[0])
                    return Response((db_user[0].id),status= status.HTTP_200_OK)
                return Response((db_user[0].id),status= status.HTTP_200_OK)
        return Response({'detail':'wrong api key'})








@api_view(['GET'])
def logout_view(request,key):
    """
    Logout API
    """
    if key == api_key:
        logout(request)
        return Response({"logged out":True})
    return Response({"detail":"wrong api key"})
