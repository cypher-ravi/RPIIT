from django.db import models
from authentication.models import User
from django.db.models.signals import post_save
from pyfcm import FCMNotification
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
    department = models.ForeignKey(Department,on_delete=models.CASCADE,blank=True, null=True)
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



def announcement_create(sender, instance, created, **kwargs):
    print('signal working')
    path_to_fcm = "https://fcm.googleapis.com"
    server_key = 'AAAAcJkoZ-I:APA91bE2NWUD-Q5O5MB8gQaLnN9cQ72hw3T_micRtdO1qPb6qSzGDJhx3iyVJyKqOTsuQujwVt04zG2MPunMmkARVTERoPVGgSI47RSCnBBSwkAZRIzim1xrbvO00Dl3oHeLjnIqTQ_q'
    message_title = "test notification"
    message_body = "Hi abhinav sir,notification Rocks!"
    result = FCMNotification(api_key=server_key).notify_single_device(registration_id='v3fLIqD2bEZdpwAOEXAFKJRUyzb2',message_title=message_title, message_body=message_body)



post_save.connect(announcement_create, sender=Announcement)



class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=225,default='',blank=True, null=True)
    father_name = models.CharField(max_length=225,default='',blank=True, null=True)
    mobile_number = models.CharField(max_length=14,default='',blank=True,null=True)
    email = models.CharField(max_length=225,default='',blank=True,null=True)
    address = models.CharField(max_length= 1000,default='',blank=True,null=True)
    age = models.CharField(max_length=20,default='',blank=True,null=True)
    semester_or_year = models.CharField(max_length =225,default='',blank=True,null=True)
    profile_submit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Student Profiles"

    def __str__(self): return self.name



class Sport(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='',blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=225,default='',blank=True, null=True)
    img = models.ImageField(upload_to='Sportevents/img',blank=True, null=True)
    co_ordinator = models.CharField(max_length=120,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sport list"

    def __str__(self): return self.name


class CulturalActivity(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='',blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=225,default='',blank=True, null=True)
    img = models.ImageField(upload_to='Cultural_activity/img',blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Cultural Activities list"

    def __str__(self): return self.name

class SocialActivity(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='',blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(auto_now=False, auto_now_add=False)
    img = models.ImageField(upload_to='Social_activity/img',blank=True, null=True)
    co_ordinator = models.CharField(max_length=120,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Social Activities list"

    def __str__(self): return self.name

class Trip(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='',blank=True, null=True)
    img = models.ImageField(upload_to='Trip/img',blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(auto_now_add=False,blank=True, null=True)
    venue = models.CharField(max_length=225,default='',blank=True, null=True)
    charges = models.CharField(max_length=225,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Trips list"

    def __str__(self): return self.name




class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    img = models.CharField(max_length=1000,default='',blank=True,null=True)
    name = models.CharField(max_length = 25)
    father_name = models.CharField(max_length = 25)
    mobile = models.CharField(max_length = 12,default='',blank=True, null=True)
    email = models.CharField(max_length = 120,default='',blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    h_qualification = models.TextField(blank=True, null=True)
    trade = models.CharField(max_length = 25,default='',blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    achivement = models.TextField(blank=True, null=True)
    certification = models.CharField(max_length = 100,default='',blank=True, null=True)
    skills = models.CharField(max_length = 100,blank=True,null=True)
    intrests = models.CharField(max_length = 100,blank=True,null=True)
    d_o_b = models.CharField(max_length = 100,blank=True,null=True)
    langauages = models.CharField(max_length = 225,blank=True,null=True)
    submit_date = models.DateTimeField(auto_now_add=True,blank=True, null=True) 

    class Meta:
        verbose_name_plural = "Student Resumes"

    def __str__(self):
        return f'{self.name} +{self.mobile}'


class PlacementCompany(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length =50)
    description = models.TextField()
    address = models.CharField(max_length = 225,default='')
    city = models.CharField(max_length = 25,default='')
    state = models.CharField(max_length =25,default='')
    added_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='Social_activity/img',blank=True, null=True)

    def __str__(self): return self.name


class AppliedJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    company = models.ForeignKey(PlacementCompany,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self): return "user id " + str(self.user.id)+ ' applied for '+ str(self.company.name)