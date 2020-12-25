from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,logout_view



urlpatterns = [
    path('register_or_login/',UserRegisterView.as_view()),
    path('logout/',logout_view),
  


]
