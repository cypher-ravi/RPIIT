from rest_framework.serializers import ModelSerializer,SerializerMethodField,DateTimeField
from .models import *
from drf_extra_fields.fields import Base64ImageField
import base64
class AnnouncementSerializer(ModelSerializer):
    announce_date = DateTimeField(format='%H:%M:%S  %d-%m-%Y',read_only=True)
    # img = SerializerMethodField(method_name='get_img')
    class Meta:
        model = Announcement
        exclude = ['department']
    

    # def get_img(self,obj):
    #     try:              
    #         image = open(obj.img.path, "rb") 
    #         data = image.read()
    #         base64_encoded_data = base64.b64encode(data)
    #         base64_message = base64_encoded_data.decode('utf-8')
    #         return base64_message
    #     except:
    #         return None 

class ResumeUploadSerializer(ModelSerializer):
    img = SerializerMethodField(method_name='get_img')
    class Meta:
        model = Resume
        fields = '__all__'
    
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
        depth = 1

class PlacementCompanySerializer(ModelSerializer):
    class Meta:
        model = PlacementCompany
        fields = '__all__'


class StudentSportDetailSerializer(ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'



class StudentCulturalActivityDetailSerializer(ModelSerializer):
    class Meta:
        model = CulturalActivity
        fields = '__all__'