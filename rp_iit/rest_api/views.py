from authentication.models import User
from django.shortcuts import get_list_or_404, render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from .models import Announcement, Department, PlacementCompany, Resume, Student
from .serializers import *
from decouple import config

api_key = config('api_key')

# Create your views here.
class AnnouncementListView(generics.GenericAPIView):
    """
    This API provides list of latest announcements ordered by date
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(phone=request.user)
            if user.exists():
                announcements = Announcement.objects.all().order_by('-announce_date')
                if not announcements:
                    return Response({'detail':'no announcements'})
                else:
                    serializer = AnnouncementSerializer(announcements,many=True)
                    return Response(serializer.data,status=status.HTTP_200_OK)  
            else:
                return Response({'detail':'user not exists'})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
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
        if kwargs['key'] == api_key:
            serializer = ResumeUploadSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'resp': 'Your Resume Uploaded Successfully','data':serializer.data})
            else:
                return Response({'resp':serializer.errors})
        else:
            return Response({'details':'wrong api key'})
    
    

class StudentProfileView(generics.GenericAPIView):
    """
    Student Profile API
    """
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer

    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=request.data['user'])
            if user.exists():
                serializer = StudentProfileSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'detail':'Student Profile created','data':user[0].session_key},status=status.HTTP_201_CREATED)
                return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
            return Response({'details':'user not exists'})
        return Response({'detail':'wrong api key'})




class ListOfCompaniesView(generics.ListAPIView):
    """
    List of companies
    """
    queryset = PlacementCompany.objects.all()
    serializer_class = PlacementCompanySerializer

class StudentDetailsView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            student_detail = Student.objects.filter(user__session_key = kwargs['pk'])
            if student_detail.exists():
                serializer = StudentProfileSerializer(student_detail,many=True)
                return Response(serializer.data)
            return Response({'detail':'no such student with this session id'})
        else:return Response({'detail':'wrong api key'})


class SportsDetailOfStudentView(generics.GenericAPIView):
    """
    API to get all sports detail of student by slug = session_key
    """
    queryset = Sport.objects.all()
    serializer_class = StudentSportDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            student = Student.objects.get(user__session_key = kwargs['pk'])
            sports_participanted_in = Sport.objects.filter(student = student)
            if sports_participanted_in.exists():
                serializer = StudentSportDetailSerializer(sports_participanted_in,many=True)
                return Response(serializer.data)
            else:return Response({'No sports participation'})
        return Response({'detail':'wrong api key'})



class CulturalActivityDetailOfStudentView(generics.GenericAPIView):
    """
    API to get all cultural activity detail of student by slug = session_key
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = StudentCulturalActivityDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            student = Student.objects.get(user__session_key = kwargs['pk'])
            cultural_activities_in = CulturalActivity.objects.filter(student = student)
            if cultural_activities_in.exists():
                serializer = StudentCulturalActivityDetailSerializer(cultural_activities_in,many=True)
                return Response(serializer.data)
            else:return Response({'No cultural participation'})
        else:
            return Response({'detail':'wrong api key'})




class UpdateStudentProfileView(generics.RetrieveUpdateAPIView):
    """
    Update student profile by its session id
    """
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    lookup_field = 'user__session_key'
    lookup_url_kwarg = 'pk'


class UpdateStudentResumeView(generics.RetrieveUpdateAPIView):
    """
        Update student resume by its session id
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer
    lookup_field = 'user__session_key'
    lookup_url_kwarg = 'pk'
