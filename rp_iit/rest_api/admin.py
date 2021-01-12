from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title','description','img',)
    list_filter = ('date' , )
    search_fields = ('title','description','department__name',)
  


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ('name',)
    
  
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','father_name','email','user',)
    list_filter = ('profile_submit_date' ,'age' )
    search_fields = ('name','user__phone',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name','father_name','mobile','email','user',)
    list_filter = ('submit_date' , )
    search_fields = ('name','user__phone',)
  


admin.site.register(PlacementCompany)



@admin.register(StudentSportProfile)
class StudentSportProfileAdmin(admin.ModelAdmin):
    list_display = ('roll_no','age','user',)
    search_fields = ('roll_no','user__phone',)




@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name',) 


@admin.register(CulturalActivity)
class CultutralAdmin(admin.ModelAdmin):
    list_display = ('name',) 

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('name',) 

@admin.register(SocialActivity)
class SocialActivityAdmin(admin.ModelAdmin):
    list_display = ('name',) 

