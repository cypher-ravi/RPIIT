from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title','description','img','announce_date')
    list_filter = ('announce_date' , )
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
class TripAdmin(admin.ModelAdmin):
    list_display = ('name',) 
