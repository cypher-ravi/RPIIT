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

#TODO:
# 1)encrypt session key
# 2)review session key storege

api_key = config('api_key')

class UserCreateAndLoginView(generics.GenericAPIView):
    """
    Register, use same session key in new session key field and
    session key field and logged in with same session key
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            db_user = User.objects.filter(phone=request.data['phone'])
            if not db_user:
                serializer = UserSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(is_verified=True)
                    return Response({'detail':'user created'},status= status.HTTP_201_CREATED)
                return Response({'detail':serializer.errors},status= status.HTTP_400_BAD_REQUEST)
            else:
                for user in db_user:
                    if user.session_key == request.data['session_key']:
                        user.new_session_key = request.data['new_session_key']
                        user.save()
                    else:
                        return Response({'previous session key not matched'})
            if db_user[0].is_verified and db_user[0].is_student:
                login(request,db_user[0])
                return Response({'logged_in':True},status= status.HTTP_200_OK)
            return Response({'user not student'})
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
