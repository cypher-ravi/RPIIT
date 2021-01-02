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
            announcements = Announcement.objects.all().order_by('-announce_date')
            if not announcements:
                return Response({'detail':'no announcements'})
            else:
                serializer = AnnouncementSerializer(announcements,many=True,context={"request": request})
                return Response(serializer.data,status=status.HTTP_200_OK)  
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
class ResumeUploadView(generics.GenericAPIView):
    """
    upload resume API
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer

    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.get(id=kwargs['pk'])
            if user !=None:
                try:
                    resume = Resume.objects.get(user=user)
                except:
                    resume = Resume.objects.none()
                if not resume:
                    serializer = ResumeUploadSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=user)
                        return Response({'detail':'Resume created'},status=status.HTTP_201_CREATED)
                    return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
                else:
                    return Response({'resume already exists'})
            return Response({'details':'user not exists'})
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
            user = User.objects.get(id=kwargs['pk'])
            if user !=None:
                try:
                    profile = Student.objects.get(user=user)
                except:
                    profile = Student.objects.none()
                if not profile:
                    serializer = StudentProfileSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=user)
                        return Response({'detail':'Student Profile created','data':user.session_key},status=status.HTTP_201_CREATED)
                    return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
                else:
                    return Response({'profile already exists'})
            return Response({'details':'user not exists'})
        return Response({'detail':'wrong api key'})




class StudentDetailsView(generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            student_detail = Student.objects.filter(user__id = kwargs['pk'])
            print('.........',student_detail)
            if student_detail.exists():
                serializer = StudentProfileSerializer(student_detail,many=True)
                return Response(serializer.data)
            return Response({'detail':'no such student with this session id'})
        else:return Response({'detail':'wrong api key'})


class SportsDetailOfStudentView(generics.ListAPIView):
    """
    API to get all sports detail of student by slug = user id
    """
    queryset = Sport.objects.all()
    serializer_class = StudentSportDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            student = Student.objects.get(user__id = kwargs['pk'])
            sports_participanted_in = Sport.objects.filter(student = student)
            if sports_participanted_in.exists():
                serializer = StudentSportDetailSerializer(sports_participanted_in,many=True,context={"request": request})
                return Response(serializer.data)
            else:return Response({'No sports participation'})
        return Response({'detail':'wrong api key'})



class CulturalActivityDetailOfStudentView(generics.ListAPIView):
    """
    API to get all cultural activity detail of student by slug = user id
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = StudentCulturalActivityDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            student = Student.objects.get(user__id = kwargs['pk'])
            cultural_activities_in = CulturalActivity.objects.filter(student = student)
            if cultural_activities_in.exists():
                serializer = StudentCulturalActivityDetailSerializer(cultural_activities_in,many=True,context={"request": request})
                return Response(serializer.data)
            else:return Response({'detail':'No cultural participation'})
        else:
            return Response({'detail':'wrong api key'})

class SocialActivityDetailOfStudentView(generics.ListAPIView):
    """
    API to get all Social activity detail of student by slug = session_key
    """
    queryset = SocialActivity.objects.all()
    serializer_class = StudentSocialActivityDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            student = Student.objects.filter(user__id = kwargs['pk'])
            if student.exists():
                social_activities_in = SocialActivity.objects.filter(student = student[0])
                if social_activities_in.exists():
                    serializer = StudentSocialActivityDetailSerializer(social_activities_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:return Response({'No social activity participation'})
            else:return Response({'detail':'no student'})
        else:
            return Response({'detail':'wrong api key'})




class UpdateStudentProfileView(generics.RetrieveUpdateAPIView):
    """
    Update student profile by its user id
    """
    queryset = Student.objects.all()
    serializer_class = StudentProfileSerializer
    lookup_field = 'user__id'
    lookup_url_kwarg = 'pk'


class UpdateStudentResumeView(generics.RetrieveUpdateAPIView):
    """
        Update student resume by its user id
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer
    lookup_field = 'user__id'
    lookup_url_kwarg = 'pk'






class CulturalActivityList(generics.ListAPIView):
    """
    API to get all cultural activity list 
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = CulturalActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            cultural_activities_in = CulturalActivity.objects.all().order_by('-date')
            serializer = CulturalActivityListSerializer(cultural_activities_in,many=True,context={"request": request})
            return Response(serializer.data)
        else:
            return Response({'detail':'wrong api key'})




class SportEventsList(generics.ListAPIView):
    """
    API to get all sports event list 
    """
    queryset = Sport.objects.all()
    serializer_class = SportListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            sports_participanted_in = Sport.objects.all().order_by('-date')
            serializer = SportListSerializer(sports_participanted_in,many=True,context={"request": request})
            return Response(serializer.data)
        return Response({'detail':'wrong api key'})



class SocialActivityList(generics.ListAPIView):
    """
    API to get all social  event list 
    """
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            social_activities_in = SocialActivity.objects.all().order_by('-date')
            serializer = SportListSerializer(social_activities_in,many=True,context={"request": request})
            return Response(serializer.data)
        return Response({'detail':'wrong api key'})



class ListOfCompaniesView(generics.ListAPIView):
    """
    List of companies
    """
    queryset = PlacementCompany.objects.all()
    serializer_class = PlacementCompanySerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            companies = PlacementCompany.objects.all()
            serializer = PlacementCompanySerializer(companies,many=True,context={"request": request})
            return Response(serializer.data)
        return Response({'detail':'wrong api key'})



class ListOfTripView(generics.ListAPIView):
    """
    List of Trips
    """
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            trips = Trip.objects.all()
            serializer = TripListSerializer(trips,many=True,context={"request": request})
            return Response(serializer.data)
        return Response({'detail':'wrong api key'})