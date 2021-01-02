from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth import authenticate, login,logout
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserCreateAndLoginSerializer as UserSerializer
from decouple import config
# Create your views here.


api_key = config('api_key')

class UserRegisterView(generics.GenericAPIView):
    """
    Register and Login API
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

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
                    return Response((serializer.data,False),status= status.HTTP_201_CREATED)
                return Response({'detail':serializer.errors})
            else:
                if db_user[0].is_verified and db_user[0].is_student:
                    db_user[0].session_key = request.data['session_key']
                    db_user[0].save()
                    login(request,db_user[0])
                    return Response({'logged_in':True},status= status.HTTP_200_OK)
                return Response((db_user[0].id,db_user[0].is_student),status= status.HTTP_200_OK)
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
