from decouple import config
from django.shortcuts import get_list_or_404, render
from django.views.decorators.csrf import csrf_exempt

from authentication.models import User
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response

from .models import Announcement, Department, PlacementCompany, Resume, Student
from .serializers import *
from django.utils import timezone
from rest_framework.decorators import api_view

api_key = config('api_key')





"""
-----------------------------------> List APIs <------------------------------------------------------------
"""
# Create your views here.
class AnnouncementListView(generics.GenericAPIView):
    """
    This API provides list of latest announcements ordered by date
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            announcements = Announcement.objects.all().order_by('-date')
            if not announcements:
                return Response({'detail':'no announcements'})
            else:
                serializer = AnnouncementSerializer(announcements,many=True,context={"request": request})
                return Response(serializer.data,status=status.HTTP_200_OK)  
        return Response(status=status.HTTP_400_BAD_REQUEST)

 
class CulturalActivityList(generics.ListAPIView):
    """
    API to get all cultural activity list 
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = CulturalActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=kwargs['user_id']).first()
            if user != None:
                student = Student.objects.filter(user=user).first()
                if student != None:  
                    cultural_activities_in = CulturalActivity.objects.all().order_by('-date').exclude(student = student)
                    serializer = CulturalActivityListSerializer(cultural_activities_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:
                        return Response({"detail":"student profile not found"})
            else:
                return Response({"dedetail":"user not found"})
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
            user = User.objects.filter(id=kwargs['user_id']).first()
            if user != None:
                student = Student.objects.filter(user=user).first()
                if student != None: 
                    sports_participanted_in = Sport.objects.all().order_by('-date').exclude(student = student)
                    serializer = SportListSerializer(sports_participanted_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:
                    return Response({"detail":"student profile not found"})
            else:
                return Response({"dedetail":"user not found"})
        return Response({'detail':'wrong api key'})



class SocialActivityList(generics.ListAPIView):
    """
    API to get all social  event list 
    """
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            user = User.objects.filter(id=kwargs['user_id']).first()
            if user != None:
                student = Student.objects.filter(user=user).first()
                if student != None:
                    social_activities_in = SocialActivity.objects.filter(approved=True).order_by('-date').exclude(student=student)
                    serializer = SocialActivityListSerializer(social_activities_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:
                    return Response({"detail":"student profile not found"})
            else:
                return Response({"dedetail":"user not found"})
        return Response({'detail':'wrong api key'})



class ListOfCompaniesView(generics.ListAPIView):
    """
    List of companies
    """
    queryset = PlacementCompany.objects.all()
    serializer_class = PlacementCompanySerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            user = User.objects.filter(id=kwargs['user_id']).first()
            if user != None:
                student = Student.objects.filter(user=user).first()
                if student != None:
                    companies = PlacementCompany.objects.all().exclude(student=student)
                    serializer = PlacementCompanySerializer(companies,many=True,context={"request": request})
                    return Response(serializer.data)
                else:
                    return Response({"detail":"student profile not found"})
            else:
                return Response({"detail":"user not found"})
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


"""
---------------------------------------->List APIs ends <----------------------------------------------------------

"""


"""
------------------------------------------>POST Request Resume ,Student Profile,Sport Profile starts<----------------------------------
"""
   
class ResumeUploadView(generics.GenericAPIView):
    """
    upload resume API
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeUploadSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=kwargs['pk'])
            if user.exists():
                try:
                    resume = Resume.objects.get(user=user[0])
                except:
                    resume = Resume.objects.none()
                if not resume:
                    serializer = ResumeUploadSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=user[0])
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
            user = User.objects.filter(id=kwargs['pk'])
            if user.exists():
                try:
                    profile = Student.objects.get(user=user[0])
                except:
                    profile = Student.objects.none()
                if not profile:
                    serializer = StudentProfileSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=user[0])
                        return Response({'detail':'Student Profile created'},status=status.HTTP_201_CREATED)
                    return Response({'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
                else:
                    return Response({'profile already exists'})
            else:
                return Response({'details':'user not exists'})
        else:
            return Response({'detail':'wrong api key'})



class StudentSportProfileView(generics.GenericAPIView):
    queryset = StudentSportProfile.objects.all()
    serializer_class = StudentSportProfileSerializer


    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=kwargs['pk'])
            if user.exists():
                serializer = StudentSportProfileSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(user=user[0])
                    return Response({"detail":"sport profile create successfully"})
                return Response({"detail":"wrong data"})
            return Response({"detail":"user not found"})
        else:return Response({"detail":"wrong api key"})


"""
--------------------------------------------->POST Request Resume ,Student Profile,Sport Profile ends<-----------------------------------
"""




"""
--------------------------------------------->Student detail APIs starts<-------------------------------------------------------------
"""

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
            student = Student.objects.filter(user__id = kwargs['pk'])
            if student.exists():
                sports_participanted_in = Sport.objects.filter(student = student[0])
                if sports_participanted_in.exists():
                    serializer = StudentSportDetailSerializer(sports_participanted_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:return Response({'No sports participation'})
            else:return Response({'detail':'not a student'})
        return Response({'detail':'wrong api key'})



class CulturalActivityDetailOfStudentView(generics.ListAPIView):
    """
    API to get all cultural activity detail of student by slug = user id
    """
    queryset = CulturalActivity.objects.all()
    serializer_class = StudentCulturalActivityDetailSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            student = Student.objects.filter(user__id = kwargs['pk'])
            if student.exists():
                cultural_activities_in = CulturalActivity.objects.filter(student = student[0])
                if cultural_activities_in.exists():
                    serializer = StudentCulturalActivityDetailSerializer(cultural_activities_in,many=True,context={"request": request})
                    return Response(serializer.data)
                else:return Response({'detail':'No cultural participation'})
            else:return Response({'detail':'not a student'})
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
            else:return Response({'detail':'not a student'})
        else:
            return Response({'detail':'wrong api key'})

class AppliedJobDetailOfStudentView(generics.ListAPIView):
    """
    API to get all applied company detail of student 
    """
    queryset = PlacementCompany.objects.all()
    serializer_class = PlacementCompanySerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            student = Student.objects.filter(user__id = kwargs['pk'])
            if student.exists():
                companies = PlacementCompany.objects.filter(student = student[0])
                if companies.exists():
                    serializer = PlacementCompanySerializer(companies,many=True,context={"request": request})
                    return Response(serializer.data)
                else:return Response({'No job application found'})
            else:return Response({'detail':'not a student'})
        else:
            return Response({'detail':'wrong api key'})

"""
----------------------------------------------->Student detail APIs ends<------------------------------------------------
"""

"""
------------------------------------------------>Update APIs Profile and Resume starts<-----------------------------------------
"""

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



"""
------------------------------------------------>Update APIs Profile and Resume ends<-----------------------------------------
"""



"""
------------------------------------------------>Past events Lists APIs starts<-----------------------------------------
"""


class ListOfPastCulturalActivityView(generics.ListAPIView):
    """
    List Of all past events including cultural activities
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


            return Response(serialize_cultural_activity.data)
            
        return Response({'detail':'wrong api key'})





class ListOfPastTripView(generics.ListAPIView):
    """
    List Of all past events including Trips
    """
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            now = timezone.now()
            trip_list = Trip.objects.filter(date__lt=now)
            serialize_trip_list = TripListSerializer(trip_list,many=True,context={"request": request})

            return Response(serialize_trip_list.data)
            
        return Response({'detail':'wrong api key'})



class ListOfPastSportView(generics.ListAPIView):
    """
    List Of all past events including sport events
    """
    queryset = Sport.objects.all()
    serializer_class = SportListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            now = timezone.now()
          
            sports_activity_list = Sport.objects.filter(date__lt=now)
            serialize_sports_activity = SportListSerializer(sports_activity_list,many=True,context={"request": request})

            return Response(serialize_sports_activity.data)
            
        return Response({'detail':'wrong api key'})



class ListOfPastSocialActivityView(generics.ListAPIView):
    """
    List Of all past events including social activity
    """
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivityListSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key: 
            # trips = Trip.objects.all()
            # serializer = TripListSerializer(trips,many=True,context={"request": request})
            # return Response(serializer.data)
            now = timezone.now()
          
            social_activity_list = SocialActivity.objects.filter(date__lt=now)
            serialize_social_activity = SocialActivityListSerializer(social_activity_list,many=True,context={"request": request})


            return Response(serialize_social_activity.data)
            
        return Response({'detail':'wrong api key'})
            

           

class PastAnnouncementListView(generics.GenericAPIView):
    """
    This API provides list of past announcements 
    """
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            now = timezone.now()
            announcements = Announcement.objects.filter(date__lt=now)
            
            serializer = AnnouncementSerializer(announcements,many=True,context={"request": request})
            return Response(serializer.data,status=status.HTTP_200_OK)  
        return Response(status=status.HTTP_400_BAD_REQUEST)

"""
------------------------------------------------>Past events Lists APIs ends<-----------------------------------------
"""

"""
------------------------------------------------>Participate APIs starts<---------------------------------------------
"""


@api_view(['GET','POST'])
def participate_cultural_activity(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == 'POST':
                user = User.objects.filter(id=kwargs['pk'])
                if user.exists():
                    student = Student.objects.filter(user=user[0])
                    if student.exists():
                        cultural_activity = CulturalActivity.objects.filter(id =kwargs['cultural_activity_id'])
                        if cultural_activity.exists():
                            cultural_activity[0].student.add(student[0])
                            cultural_activity[0].save()
                            return Response({"detail":"applied for culturalactivity"})
                        else:
                            return Response({"detail":"cultural activity not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})


@api_view(['GET','POST'])
def cancel_cultural_activity(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk']).first()
                if user != None:
                    student = Student.objects.filter(user=user).first()
                    if student != None:
                        cultural_activity = CulturalActivity.objects.filter(id =kwargs['cultural_activity_id']).first()
                        if cultural_activity != None:
                            cultural_activity.student.remove(student)
                            cultural_activity.save()
                            return Response({"detail":"cancelled cultural activity"})
                        else:
                            return Response({"detail":"cultural activity not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})




@api_view(['GET','POST'])
def participate_sport_event(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk'])
                if user.exists():
                    student = Student.objects.filter(user=user[0])
                    if student.exists():
                        sport_event = Sport.objects.filter(id =kwargs['sport_event_id'])
                        if sport_event.exists():
                            sport_event[0].student.add(student[0])
                            sport_event[0].save()
                            return Response({"detail":"applied for sport"})
                        else:
                            return Response({"detail":"sport not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})


@api_view(['GET','POST'])
def cancel_sport_event(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk']).first()
                if user != None:
                    student = Student.objects.filter(user=user).first()
                    if student != None:
                        sport_event = Sport.objects.filter(id =kwargs['sport_event_id']).first()
                        if sport_event != None:
                            sport_event.student.remove(student)
                            sport_event.save()
                            return Response({"detail":"cancelled sport event"})
                        else:
                            return Response({"detail":"sport event not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})






@api_view(['GET','POST'])
def participate_social_activity(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk'])
                if user.exists():
                    student = Student.objects.filter(user=user[0])
                    if student.exists():
                        social_activities = SocialActivity.objects.filter(id =kwargs['social_activity_id'])
                        if social_activities.exists():
                            social_activities[0].student.add(student[0])
                            social_activities[0].save()
                            return Response({"detail":"applied for social activity"})
                        else:
                            return Response({"detail":"social activity not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})



@api_view(['GET','POST'])
def cancel_social_activity(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk']).first()
                if user != None:
                    student = Student.objects.filter(user=user)
                    if student != None:
                        social_activities = SocialActivity.objects.filter(id =kwargs['social_activity_id']).first()
                        if social_activities != None:
                            social_activities.student.remove(student[0])
                            social_activities.save()
                            return Response({"detail":"cancelled social activity"})
                        else:
                            return Response({"detail":"social activity not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})



@api_view(['GET','POST'])
def apply_for_job(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk'])
                if user.exists():
                    student = Student.objects.filter(user=user[0])
                    if student.exists():
                        company = PlacementCompany.objects.filter(id =kwargs['company_id'])
                        if company.exists():
                            if PlacementCompany.objects.filter(student=student[0],id=company[0].id).exists():
                                return Response({"detail": "already applied"})
                            else:
                                company[0].student.add(student[0])
                                company[0].save()
                                return Response({"detail":"applied for job"})
                        else:
                            return Response({"detail":"company not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})



@api_view(['GET','POST'])
def cancel_applied_job(request, *args, **kwargs):
        if kwargs['key'] == api_key:
            if request.method == "POST":
                user = User.objects.filter(id=kwargs['pk'])
                if user.exists():
                    student = Student.objects.filter(user=user[0])
                    if student.exists():
                        company = PlacementCompany.objects.filter(id =kwargs['company_id'])
                        if company.exists():
                            company[0].student.remove(student[0])
                            company[0].save()
                            return Response({"detail":"cancel applied job"})
                        else:
                            return Response({"detail":"company not found"})
                    return Response({"detail":"student not found"})
                return Response({"detail":"user not found"})
            else:
                return Response({"detail":"method not allowed"})
        else:
            return Response({"detail":"wrong api key"})
"""
------------------------------------------------>Participate APIs ends<---------------------------------------------
"""

#for adding social activity by student and added after approvel of admin 
class AddSocialActivityRequestHandler(generics.GenericAPIView):
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivityRequestSerializer


    def post(self, request, *args, **kwargs):
        if kwargs['key'] == api_key:
            user = User.objects.filter(id=kwargs['pk'])
            if user.exists():
                serializer = SocialActivityRequestSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({"detail":"added to social activity"})
                else:return Response(serializer.errors)
            else:return Response({"detail":"user not found"})
        else:return Response({"detail":"wrong api key"})
                


"""
-------------------------------------------> Extra Uses APIs starts<-----------------------------------------------------
"""

class StudentInfoView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer()

    def get(self,request, *args,**kwargs):

        if kwargs['key'] == api_key: 
            user = User.objects.filter(phone=kwargs['phone'])
            if user.exists():    
                resume = Resume.objects.filter(user=user[0])
                student = Student.objects.filter(user=user[0])
                if not resume:
                    resume_submission = False
                else:
                    resume_submission = True
                if not student:
                    student_profile = False
                else:
                    student_profile = True

                if student_profile == True:
                    return Response({'user_id':user[0].id,'name':student[0].name,'student_by_admin':user[0].is_student,'student_profile':student_profile,'resume':resume_submission})
                return Response({'user_id':user[0].id,'student_by_admin':user[0].is_student,'student_profile':student_profile,'resume':resume_submission})
            else:
                return Response({"detail":'user not exists'})







"""
-------------------------------------------> Extra Uses APIs ends<-----------------------------------------------------
"""


class AddDummyData(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        from .fakedata import Dummy
        Dummy().addData(kwargs['iterations'])
        return Response({"detail": 'Data Added successfully'})


class DeleteData(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        from .fakedata import Dummy
        Dummy().deleteData()
        return Response({"detail": 'Data Deleted successfully'})