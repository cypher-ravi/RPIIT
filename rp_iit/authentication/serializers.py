from rest_framework import serializers
from .models import User



class UserCreateAndLoginSerializer(serializers.ModelSerializer):
    session_key = serializers.CharField()
    class Meta:
        model = User
        fields = ['id','phone','session_key']

 
