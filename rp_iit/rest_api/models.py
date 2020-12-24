from django.db import models
from authentication.models import User
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,default='')

    class Meta:
        verbose_name_plural = ("Departments")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Department_detail", kwargs={"pk": self.pk})


class Announcement(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    announce_date = models.DateTimeField()
    title = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    img = models.ImageField(upload_to='Announcements/img')
    
    

    class Meta:
        verbose_name_plural = "Announcements list"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Announcement_detail", kwargs={"pk": self.pk})



class Sport(models.Model):
    name = models.CharField(max_length=50,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sport list"

    def __str__(self): return self.name


class CulturalActivity(models.Model):
    name = models.CharField(max_length=50,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cultural Activities list"

    def __str__(self): return self.name

class SocialActivity(models.Model):
    name = models.CharField(max_length=50,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Social Activities list"

    def __str__(self): return self.name

class Trip(models.Model):
    name = models.CharField(max_length=50,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Trips list"

    def __str__(self): return self.name




class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=225,default='',blank=True, null=True)
    father_name = models.CharField(max_length=225,default='',blank=True, null=True)
    mobile_number = models.CharField(max_length=14,default='',blank=True,null=True)
    email = models.EmailField()
    address = models.CharField(max_length= 1000,default='',blank=True,null=True)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    semester_or_year = models.CharField(max_length =225,default='',blank=True,null=True)
    profile_submit_date = models.DateTimeField(auto_now_add=True)
    sports_participanted_in = models.ForeignKey(Sport,on_delete=models.CASCADE,blank=True, null=True)
    cultural_activities_in = models.ForeignKey(CulturalActivity,on_delete=models.CASCADE,blank=True, null=True)
    social_activities_in = models.ForeignKey(SocialActivity,on_delete=models.CASCADE,blank=True, null=True)
    trips_participanted_in = models.ForeignKey(Trip,on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Student Profiles"

    def __str__(self): return self.name



class Resume(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    img = models.ImageField(upload_to='Studentresume/img',blank=True,null=True)
    name = models.CharField(max_length = 25)
    father_name = models.CharField(max_length = 25)
    mobile = models.CharField(max_length = 12)
    email = models.EmailField()
    address = models.TextField()
    h_qualification = models.TextField()
    trade = models.CharField(max_length = 25)
    work_experience = models.TextField()
    projects = models.TextField()
    achivement = models.TextField()
    certification = models.CharField(max_length = 100)
    skills = models.CharField(max_length = 100)
    intrests = models.CharField(max_length = 100)
    submit_date = models.DateTimeField(auto_now_add=True,blank=True, null=True) 

    class Meta:
        verbose_name_plural = "Student Resumes"

    def __str__(self):
        return self.name


class PlacementCompany(models.Model):
    name = models.CharField(max_length =50)
    description = models.TextField()
    address = models.CharField(max_length = 225,default='')
    city = models.CharField(max_length = 25,default='')
    state = models.CharField(max_length =25,default='')
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name


