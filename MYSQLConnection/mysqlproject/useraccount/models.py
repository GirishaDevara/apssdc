from django.db import models

# Create your models here.
class Userregister(models.Model):
	fullname = models.CharField(max_length=100)
	mailid = models.EmailField(unique=True)
	password = models.CharField(max_length=150,default='password@123')
	image = models.ImageField(upload_to='profilepics/')
	def __str__(self):
		return self.fullname