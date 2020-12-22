from django.contrib import admin
from django.urls import path,include
from .views import UserCreateAndLoginView



urlpatterns = [
    path('register_and_login/',UserCreateAndLoginView.as_view() ),
  


]
