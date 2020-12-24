from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,logout_view,LoginView



urlpatterns = [
    path('register/',UserRegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('logout/',logout_view),
  


]
