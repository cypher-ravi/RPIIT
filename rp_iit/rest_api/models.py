from django.db import models

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
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Announcement_detail", kwargs={"pk": self.pk})

class Resume(models.Model):
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

    def __str__(self):
        return self.name