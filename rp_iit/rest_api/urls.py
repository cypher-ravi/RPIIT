from django.contrib import admin
from django.urls import path,include
from .views import AnnouncementListView,DepartmentListView

urlpatterns = [
    path('announcements/<str:slug>/',AnnouncementListView.as_view() ),
    path('departments/',DepartmentListView.as_view() ),


]
