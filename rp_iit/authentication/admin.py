from django.contrib import admin
from .models import User
from django.urls import reverse
from django.utils.http import urlencode
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "is_verified",'is_student','registered_date')     
    list_filter = ("phone", 'is_student','registered_date')  
    search_fields = ("phone", )

    


    # def view_student_link(self, obj):
    #     url =  (
    #         reverse('rest_api:Student')
    #         + "?"
    #         + urlencode({'user_id': f"{obj.id}"})    
    #     )
    #     return format_html('<a href="{}">{} Student</a>',url)
    # view_student_link.short_description = "Student"