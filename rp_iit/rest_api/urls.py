from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'rest_api'

urlpatterns = [
    path('announcements/',AnnouncementListView.as_view()),

    path('upload_resume/<str:pk>', ResumeUploadView.as_view()),
    path('update_student_resume/<str:pk>', UpdateStudentResumeView.as_view()),
    
    
    path('student_profile/<str:pk>', StudentProfileView.as_view()),
    path('update_student_profile/<str:pk>', UpdateStudentProfileView.as_view()),

    path('student_detail/<str:pk>', StudentDetailsView.as_view()),
    path('student_sports_detail/<str:pk>', SportsDetailOfStudentView.as_view()),
    path('student_cultural_activity_detail/<str:pk>', CulturalActivityDetailOfStudentView.as_view()),
    path('student_social_activity_detail/<str:pk>', SocialActivityDetailOfStudentView.as_view()),

    path('list_of_companies/', ListOfCompaniesView.as_view()),
    path('list_of_cultural_activties/', CulturalActivityList.as_view()),
    path('list_of_social_activties/', SocialActivityList.as_view()),
    path('list_of_sport_events/', SportEventsList.as_view()),
    



]
