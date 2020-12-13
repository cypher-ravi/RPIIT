from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Announcement,Department
from drf_extra_fields.fields import Base64ImageField
import base64
class AnnouncementSerializer(ModelSerializer):
    img = SerializerMethodField()
    class Meta:
        model = Announcement
        exclude = ['department']
    

    def get_img(self,obj):
        try:              
            image = open(obj.img.path, "rb") 
            data = image.read()
            base64_encoded_data = base64.b64encode(data)
            base64_message = base64_encoded_data.decode('utf-8')
            return base64_message
        except:
            return None 




 
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'