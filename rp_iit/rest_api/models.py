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
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    title = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    img = models.ImageField(upload_to='Announcements/img' ,default='')
    
    

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
    img = models.ImageField(upload_to='Sportevents/img', null=True, default='')
    co_ordinator = models.CharField(max_length=120,default='',blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sport list"

    def __str__(self): return self.name


class CulturalActivity(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='')
    date = models.DateField()
    time  = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=225,default='',blank=True, null=True)
    img = models.ImageField(upload_to='Cultural_activity/img', null=True, default='')
    description = models.TextField(blank=True, null=True)
   

    class Meta:
        verbose_name_plural = "Cultural Activities list"

    def __str__(self): return self.name

class SocialActivity(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='')
    date = models.DateField()
    time  = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    img = models.ImageField(upload_to='Social_activity/img',default='')
    co_ordinator = models.CharField(max_length=120,default='',blank=True, null=True)
    approved = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = "Social Activities list"

    def __str__(self): return self.name

class Trip(models.Model):
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length=50,default='',blank=True, null=True)
    img = models.ImageField(upload_to='Trip/img', null=True, default='')
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
    student = models.ManyToManyField(Student,blank=True)
    name = models.CharField(max_length =50)
    description = models.TextField()
    address = models.CharField(max_length = 225,default='')
    city = models.CharField(max_length = 25,default='')
    state = models.CharField(max_length =25,default='')
    added_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='PlacementCompany/img', null=True, default='')

    def __str__(self): return self.name




class StudentSportProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    roll_no = models.CharField(max_length=25,primary_key=True,unique=True)
    age = models.CharField(max_length=25,default='')
    weight = models.CharField(max_length=25,default='')
    height = models.CharField(max_length=25,default='')
    interest = models.CharField(max_length=255,default='')

    class Meta:
        verbose_name_plural = "Students Sport Profile Details"

    def __str__(self):
        return self.roll_no


class Comment(models.Model):
    student_sender =  models.ForeignKey(Student,on_delete=models.CASCADE,help_text="Student who commented",related_name='commenter')
    student_comment_reciever =  models.ForeignKey(Student,on_delete=models.CASCADE,help_text="Student who received comment",related_name='receiver')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)    

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return self.student_sender.name + " commented on profile of " + self.student_comment_reciever.name


    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})


class Emagazine(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    name_of_topic = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='Emagazine/img', null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)




    class Meta:
        verbose_name = ("E-magazine")
        verbose_name_plural = ("E-magazines")

    def __str__(self):
        return self.name_of_topic

    def get_absolute_url(self):
        return reverse("E-magazine_detail", kwargs={"pk": self.pk})


class YearBookProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=225,default='')
    email = models.CharField(max_length=225,default='')
    phone = models.CharField(max_length=225,default='',blank=True, null=True)
    department = models.CharField(max_length=225,default='',blank=True, null=True)
    i_will_always_remember = models.CharField(max_length =500,default='',blank=True, null=True)
    your_best_hidden_talent = models.CharField(max_length=500,default='',blank=True, null=True)
    dream_in_life = models.CharField(max_length=500,default='',blank=True, null=True)
    what_makes_you_laugh_the_most = models.CharField(max_length=500,default='',blank=True, null=True)
    describe_your_final_year = models.CharField(max_length=500,default='',blank=True, null=True)
    fav_curc_activity = models.CharField(max_length=500,default='',blank=True, null=True)
    most_emb_moment =  models.CharField(max_length=500,default='',blank=True, null=True)
    image = models.ImageField(upload_to='YearBookProfileImg',blank=True, null=True)

    
    

    class Meta:
        verbose_name = ("YearBookProfile")
        verbose_name_plural = ("YearBookProfiles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("YearBookProfile_detail", kwargs={"pk": self.pk})
