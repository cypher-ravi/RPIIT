from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('announcements/<str:slug>/',AnnouncementListView.as_view() ),
    path('departments/',DepartmentListView.as_view() ),
    path('resume/', ResumeUploadView.as_view()),
    path('student_profile/', StudentProfileView.as_view()),
    path('list_of_companies/', ListOfCompaniesView.as_view()),
    # path('update_student_profile/<str:pk>', UpdateStudentProfile.as_view()),



]
