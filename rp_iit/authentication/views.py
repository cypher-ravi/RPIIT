from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserCreateAndLoginSerializer as UserSerializer

# Create your views here.

class UserCreateAndLoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(phone=request.data['phone'])
        if not user:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'detail':'user created'},status= status.HTTP_201_CREATED)
            return Response({'detail':serializer.errors},status= status.HTTP_400_BAD_REQUEST)
        session_key = request.data['session_key']
        for i in user:
            i.session_key = session_key
            i.save()
        return Response({'logged_in':True},status= status.HTTP_200_OK)