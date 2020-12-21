from django.contrib import admin
from django.urls import path,include
from .views import AnnouncementListView, DepartmentListView, ResumeUploadView

urlpatterns = [
    path('announcements/<str:slug>/',AnnouncementListView.as_view() ),
    path('departments/',DepartmentListView.as_view() ),
    path('resume/', ResumeUploadView.as_view()),


]
