from django.contrib import admin
from django.urls import path,include
from .views import UserCreateAndLoginView,logout_view



urlpatterns = [
    path('register_and_login/',UserCreateAndLoginView.as_view() ),
    path('logout/',logout_view),
  


]
