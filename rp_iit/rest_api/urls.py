from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'rest_api'

urlpatterns = [
    path('announcements/<str:slug>/',AnnouncementListView.as_view()),
    path('departments/',DepartmentListView.as_view()),

    path('upload_resume/', ResumeUploadView.as_view()),
    path('update_student_resume/<str:pk>', UpdateStudentResumeView.as_view()),
    
    
    path('student_profile/', StudentProfileView.as_view()),
    path('update_student_profile/<str:pk>', UpdateStudentProfileView.as_view()),

    path('student_corner/<str:pk>', StudentDetailsView.as_view()),
    path('student_sports_detail/<str:pk>', SportsDetailOfStudentView.as_view()),
    path('student_cultural_activity_detail/<str:pk>', CulturalActivityDetailOfStudentView.as_view()),

    path('list_of_companies/', ListOfCompaniesView.as_view()),
    



]
