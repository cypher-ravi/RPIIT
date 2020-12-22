from django.shortcuts import render,get_list_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Announcement, Department, Resume,Student,PlacementCompany
from authentication.models import User
from .serializers import *

from rest_framework import mixins

# Create your views here.
class AnnouncementListView(generics.GenericAPIView):
    """
    This API provides list of announcements by providing slug=department name
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(phone=request.user)
        if user.exists():
            if Department.objects.filter(name=kwargs['slug']).exists():
                announcements = Announcement.objects.filter(department__name=kwargs['slug']).order_by('-announce_date')
                if not announcements:
                    return Response({'detail':'no announcements'})
                else:
                    serializer = AnnouncementSerializer(announcements,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)  
            else:
                return Response({'detail':'no such department'})
        else:
            return Response({'detail':'user not exists'})
    
class DepartmentListView(generics.ListAPIView):
    """
    List of departments
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    
class ResumeUploadView(generics.GenericAPIView):
    """
    upload resume API
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResumeUploadSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'resp': 'Your Resume Uploaded Successfully','data':serializer.data})
        else:
            return Response({'resp':serializer.errors})
    


class StudentProfileView(generics.GenericAPIView):
    """
    Student Profile API
    """
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data['user'])
        if user.exists():
            serializer = StudentProfileSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'detail':'Student Profile created','data':user[0].session_key},status=status.HTTP_201_CREATED)
            return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
        return Response({'details':'user not exists'})

# class UpdateStudentProfile(generics.UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentProfileSerializer
#     # permission_classes = (permissions.IsAuthenticated,)

#     def update(self, request, *args, **kwargs):
#         lookup = self.user.session_key
#         instance = self.get_object()
#         instance.save()

#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response(serializer.data)


class ListOfCompaniesView(generics.ListAPIView):
    """
    List of companies
    """
    queryset = PlacementCompany.objects.all()
    serializer_class = PlacementCompanySerializer

