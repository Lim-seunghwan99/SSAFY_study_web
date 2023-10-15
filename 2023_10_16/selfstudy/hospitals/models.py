from django.db import models
from mtm import settings
from django.contrib.auth.models import AbstractUser
# hospitals/models.py

class Doctor(models.Model):
	name = models.TextField()
	
	def __str__(self):
		return f'{self.pk}번 의사 {self.name}'

# class Patient(models.Model):
# 	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
# 	name = models.TextField()

# 	def __str__(self):
# 		return f'{self.pk}번 환자 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
	
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 중개모델 작성
class Reservation(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
	

class Person(models.Model):
	friends = models.ManyToManyField('self')
	

class Article(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
	title = models.CharField(max_length=10)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	

class User(AbstractUser):
	pass