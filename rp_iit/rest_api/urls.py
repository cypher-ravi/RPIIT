from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'rest_api'

urlpatterns = [
    path('announcements/',AnnouncementListView.as_view()),

    path('upload_resume/<str:pk>', ResumeUploadView.as_view()),
    path('update_student_resume/<str:pk>', UpdateStudentResumeView.as_view()),
    
    
    path('student_profile/<str:pk>', StudentProfileView.as_view()),
    path('student_sport_profile/<str:pk>', StudentSportProfileView.as_view()),
    path('update_student_profile/<str:pk>', UpdateStudentProfileView.as_view()),

    path('student_detail/<str:pk>', StudentDetailsView.as_view()),
    path('student_sports_detail/<str:pk>', SportsDetailOfStudentView.as_view()),
    path('student_cultural_activity_detail/<str:pk>', CulturalActivityDetailOfStudentView.as_view()),
    path('student_social_activity_detail/<str:pk>', SocialActivityDetailOfStudentView.as_view()),
    path('student_applied_job_detail/<str:pk>', AppliedJobDetailOfStudentView.as_view()),

    path('list_of_companies/<str:user_id>/', ListOfCompaniesView.as_view()),
    path('list_of_cultural_activties/<str:user_id>/', CulturalActivityList.as_view()),
    path('list_of_social_activties/<str:user_id>/', SocialActivityList.as_view()),
    path('list_of_sport_events/<str:user_id>/', SportEventsList.as_view()),
    path('list_of_trips/', ListOfTripView.as_view()),
    


    path('list_of_past_cultural_activity/', ListOfPastCulturalActivityView.as_view()),
    path('list_of_past_social_activity/', ListOfPastSocialActivityView.as_view()),
    path('list_of_past_sport_events/', ListOfPastSportView.as_view()),
    path('list_of_past_trips/', ListOfPastTripView.as_view()),
    path('list_of_past_announcements/',PastAnnouncementListView.as_view()),


    path('student_info/<str:phone>', StudentInfoView.as_view()),

  
    path('apply_job/<str:pk>/<str:company_id>', apply_for_job),#apply job
    path('cancel_applied_job/<str:pk>/<str:company_id>', cancel_applied_job),#cancel apply job

    path('participate_cultural_activity/<str:pk>/<str:cultural_activity_id>', participate_cultural_activity),#apply cultural activity
    path('cancel_cultural_activity/<str:pk>/<str:cultural_activity_id>', cancel_cultural_activity),#cancel cultural activity
    
    path('participate_sport_event/<str:pk>/<str:sport_event_id>', participate_sport_event),#apply sport
    path('cancel_sport_event/<str:pk>/<str:sport_event_id>', cancel_sport_event),#cancel sport


    path('participate_social_activity/<str:pk>/<str:social_activity_id>', participate_social_activity),#apply social activity
    path('cancel_social_activity/<str:pk>/<str:social_activity_id>', cancel_social_activity),#cancel social activity
    
    path('add_social_activity/<str:pk>/', AddSocialActivityRequestHandler.as_view()),#apply sport

    path('add_dummy_data/<int:iterations>', AddDummyData.as_view()),
    path('delete_data', DeleteData.as_view()),
]
