from decouple import config
from django.shortcuts import get_list_or_404, render
from django.views.decorators.csrf import csrf_exempt

from authentication.models import User
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from .models import Announcement, Department, PlacementCompany, Resume, Student
from .serializers import *
from django.utils import timezone

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

    @csrf_exempt
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

    @csrf_exempt
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
                        return Response({'detail':'Student Profile created'},status=status.HTTP_201_CREATED)
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



class ListOfPastEventsView(generics.ListAPIView):
    """
    List Of all past events including cultural activities,social activities,sport activities,trip events
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = CulturalActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            # trips = Trip.objects.all()
            # serializer = TripListSerializer(trips,many=True,context={"request": request})
            # return Response(serializer.data)
            now = timezone.now()
            cultural_activity= CulturalActivity.objects.filter(date__lt=now)
            serialize_cultural_activity = CulturalActivityListSerializer(cultural_activity,many=True,context={"request": request})

            social_activity_list = SocialActivity.objects.filter(date__lt=now)
            serialize_social_activity = SocialActivityListSerializer(social_activity_list,many=True,context={"request": request})

            sports_activity_list = Sport.objects.filter(date__lt=now)
            serialize_sports_activity = SportListSerializer(sports_activity_list,many=True,context={"request": request})

            trip_list = Trip.objects.filter(date__lt=now)
            serialize_trip_list = TripListSerializer(trip_list,many=True,context={"request": request})

            return Response((serialize_cultural_activity.data,serialize_social_activity.data,serialize_sports_activity.data,serialize_trip_list.data))
            
        return Response({'detail':'wrong api key'})



class StudentInfoView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer()

    def get(self,request, *args,**kwargs):

        if kwargs['key'] == api_key: 
            user = User.objects.filter(id=kwargs['user_id'])
            if not user.exists():
                return Response({'user no exists'})
            else:
                
                profile = Student.objects.filter(user=user[0])
                resume = Resume.objects.filter(user=user[0])

                if not  profile:
                    is_student = False
                else:
                    is_student = True


                if not resume:
                    resume_submission = False
                else:
                    resume_submission = True

                return Response({'user_id':user[0].id,'student':is_student,'resume':resume_submission})


class ApplyJobView(generics.GenericAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = ApplyJobViewSerializer

    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=kwargs['pk'])

            if user.exists():
                if not AppliedJob.objects.filter(user=user[0]).exists():
                    company = PlacementCompany.objects.filter(id=kwargs['company_id'])
                    if company:
                        data = {
                            'company': company,
                            'user': user
                        }
                        serializer = ApplyJobViewSerializer(data=data)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save(user=user[0],company=company[0])
                            return Response({'detail':'job applied successfully'})
                        return Response(serializer.errors)
                    else:
                        return Response({'detail':'company not found'})
                else:return Response({'detail':'user already applied for this company'})
            else:return Response({'detail':'user not exists'})
        return Response({'wrong api key'})