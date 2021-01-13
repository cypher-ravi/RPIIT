from faker import Faker
import random
from rest_api.models import *
from authentication.models import *


class Dummy():
	def addData(self, iterations):
		f = Faker()
		print("inserting Dummy Data into Database ...:D")

		for _ in range(0, iterations):

			obj = User()
			obj.phone = f.phone_number()
			obj.session_key = f.md5()
			obj.is_active = f.boolean()
			obj.is_staff = f.boolean()
			obj.is_verified =f.boolean()
			obj.registered_date = f.date()
			obj.is_student = f.boolean()
			obj.save()

			 # --------------------------------------

			Departments = ['Cse', 'Mechanical', 'Electronics', 'IC', 'Civil']
			department_obj =  Department()
			department_obj.name = Departments[random.randint(0, 4)]
			department_obj.save()
			 
			announcement_obj = Announcement()
			announcement_obj.department = department_obj
			announcement_obj.date = f.date()
			announcement_obj.time  = f.time()
			self.title = f.text()
			announcement_obj.title = self.title[:20]
			announcement_obj.description = self.title
			announcement_obj.img = f.image_url()
			announcement_obj.save()


			student_obj = Student()
			student_obj.user = obj
			student_obj.name = f.first_name()
			student_obj.father_name = f.first_name()
			student_obj.mobile_number = f.phone_number()
			student_obj.email = f.email()
			student_obj.address = f.address()
			student_obj.age = random.randint(16,27)
			student_obj.semester_or_year = random.randint(2015,2021)
			student_obj.profile_submit_date = f.date()
			student_obj.save()
			    


			sports_list = ['Football', 'Cricket', 'Hockey', 'Tenis', 'BasketBall']
			sport_obj =Sport()
			sport_obj.name = sports_list[random.randint(0,4)]
			sport_obj.date = f.date()
			sport_obj.time  = f.time()
			sport_obj.venue = 'College'
			sport_obj.co_ordinator = f.first_name()
			sport_obj.save()
			sport_obj.student.add(student_obj)


			cultural_activity_object = CulturalActivity()
			cultural_activity_object.name = f'Test Event {random.randint(1,999)}'
			cultural_activity_object.date = f.date()
			cultural_activity_object.time  = f.time()
			cultural_activity_object.venue = 'College'
			cultural_activity_object.description = f.text()  
			cultural_activity_object.save()
			cultural_activity_object.student.add(student_obj)
			  

			social_activity_obj =  SocialActivity()
			social_activity_obj.name = f.first_name()
			social_activity_obj.date = f.date()
			social_activity_obj.time  = f.time()
			social_activity_obj.description = f.text()
			social_activity_obj.co_ordinator = f.first_name()
			social_activity_obj.approved = f.boolean()
			social_activity_obj.save()
			social_activity_obj.student.add(student_obj)


			trip_obj =  Trip()
			trip_obj.name = f.first_name()
			trip_obj.date = f.date()
			trip_obj.time  = f.time()
			trip_obj.venue = 'college'
			trip_obj.charges = random.randint(1000, 10000)
			trip_obj.save()
			trip_obj.student.add(student_obj)


			resume_obj = Resume()
			resume_obj.user = obj
			resume_obj.name = f.first_name()
			resume_obj.father_name = f.first_name()
			resume_obj.mobile = f.phone_number()
			resume_obj.email = f.email()
			resume_obj.address = f.address()
			resume_obj.h_qualification = 'test h_qualification'
			resume_obj.trade = Departments[random.randint(0,4)]
			resume_obj.projects = 'bot management system'
			resume_obj.certification = 'test certificate'
			resume_obj.skills = 'test skills'
			resume_obj.intrests = 'reading'
			resume_obj.d_o_b = f.date()
			resume_obj.langauages = 'English/Hindi'
			resume_obj.save()
			   


			placement_company_obj = PlacementCompany()
			placement_company_obj.name = f.first_name()
			placement_company_obj.description = f.text()
			placement_company_obj.address = f.address()
			placement_company_obj.city = f.city()
			placement_company_obj.state = f.state()
			placement_company_obj.save()
			placement_company_obj.student.add(student_obj) 




			student_profile_obj = StudentSportProfile()
			student_profile_obj.user = obj
			student_profile_obj.roll_no = random.randint(111111,999999)
			student_profile_obj.age = random.randint(16, 27)
			student_profile_obj.weight = random.randint(40,200)
			student_profile_obj.height = random.randint(4, 8)
			student_profile_obj.interest = 'test'
			student_profile_obj.save()
	
	def deleteData(self):
		Department.objects.all().delete()

		obj = User.objects.all()
		for i in range(0, len(obj)):
			if obj[i].phone == '9999999999':
				continue
			obj[i].delete()

		PlacementCompany.objects.all().delete()
		StudentSportProfile.objects.all().delete()
		Resume.objects.all().delete()
		Trip.objects.all().delete()
		SocialActivity.objects.all().delete()
		CulturalActivity.objects.all().delete()
		Sport.objects.all().delete()
		Student.objects.all().delete()
		Announcement.objects.all().delete()
