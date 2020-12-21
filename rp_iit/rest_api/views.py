from django.shortcuts import render,get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Announcement, Department, Resume
from .serializers import AnnouncementSerializer, DepartmentSerializer, ResumeUploadSerializer

# Create your views here.
class AnnouncementListView(generics.GenericAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        if Department.objects.filter(name=kwargs['slug']).exists():
            announcements = Announcement.objects.filter(department__name=kwargs['slug']).order_by('-announce_date')
            if not announcements:
                return Response({'detail':'no announcements'})
            else:
                serializer = AnnouncementSerializer(announcements,many=True)
                return Response(serializer.data,status=status.HTTP_200_OK)  
        else:
            return Response({'detail':'no such department'})
    
class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    
class ResumeUploadView(generics.GenericAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = ResumeUploadSerializer(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            # Above is Same for below !
            # name = request.data.get('name')
            # father_name = request.data.get('father_name')
            # mobile = request.data.get('mobile')
            # email = request.data.get('email')
            # address = request.data.get('address')
            # h_qualification = request.data.get('h_qualification')
            # trade = request.data.get('trade')
            # work_experience = request.data.get('work_experience')
            # projects = request.data.get('projects')
            # achivement = request.data.get('achivement')
            # certification = request.data.get('certification')
            # skills = request.data.get('skills')
            # intrests = request.data.get('intrests')

            # obj = Resume(name = name, father_name=father_name, mobile = mobile, emial = email, 
            #                 address = address, h_qualification = h_qualification, trade = trade,
            #                 work_experience = work_experience, projects = projects, achivement = achivement,
            #                 certification = certification, skills = skills, intrests = intrests)
            # obj.save()
                return Response({'resp': 'Your Resume Uploaded Successfully','data':serializer.data})
        except:
            return Response({'resp': 'An Erorr Ocuured While Uploading Please Try Again!'})


