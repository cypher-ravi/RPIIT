from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'Payment_gateway'

urlpatterns = [
    path('payu/',payu_checkout,name='payu_checkout'),
    path('success',payu_success),
    path('failure',payu_failure),
    path('verify_and_pay/<str:user_id>/<str:amount>/<str:trip_id>',verify_user_and_amount),
]