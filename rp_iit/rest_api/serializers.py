from rest_framework.serializers import ModelSerializer,SerializerMethodField,DateTimeField
from .models import *
from drf_extra_fields.fields import Base64ImageField
import base64
from rest_framework import status


class AnnouncementSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = Announcement
        exclude = ['department']
    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None

class ResumeUploadSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_img')
    class Meta:
        model = Resume
        exclude = ['user']
    
    def get_img(self,obj):
        try:              
            image = open(obj.img.path, "rb") 
            data = image.read()
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
            return base64_message
        except:
            return None 

        

class StudentProfileSerializer(ModelSerializer):
    class Meta:
        model = Student
        exclude = ['user']
       

class PlacementCompanySerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = PlacementCompany
        exclude = ['student']


    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None

    def get_img(self,obj):
        try:              
            image = open(obj.img.path, "rb") 
            data = image.read()
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
            return base64_message
        except:
            return None 


class StudentSportDetailSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = Sport
        exclude = ('student',)

    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None

class StudentCulturalActivityDetailSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = CulturalActivity
        exclude = ('student',)

    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None


class StudentSocialActivityDetailSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = SocialActivity
        exclude = ('student',)


    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None


class SportListSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = Sport
        exclude = ['student']

    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None

class CulturalActivityListSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')
    class Meta:
        model = CulturalActivity
        exclude = ['student']
    
   
    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None



class SocialActivityListSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')

    class Meta:
        model = SocialActivity
        exclude = ['student']

    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None


class TripListSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_photo_url')

    class Meta:
        model = Trip
        exclude = ['student']

    def get_photo_url(self, obj):
        try:
            request = self.context.get('request')
            photo_url = obj.img.url
            return request.build_absolute_uri(photo_url)
        except:
            return None



class StudentInfoSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentSportProfileSerializer(ModelSerializer):
    class Meta:
        model = StudentSportProfile
        exclude = ['user']
        




class CulturalActivityParticipantSerializer(ModelSerializer):
    """
    Serializer for student participation
    """
    class Meta:
        model = CulturalActivity
        fields = ['student_id']



class SocialActivityRequestSerializer(ModelSerializer):
    img = Base64ImageField()
    class Meta:
        model = SocialActivity
        exclude = ['approved','student']
    


