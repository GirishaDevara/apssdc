from django.db import models

# Create your models here.
class Userregister(models.Model):
	fullname = models.CharField(max_length=100)
	mailid = models.EmailField()
	password = models.CharField(max_length=100)
	image = models.ImageField(upload_to='profilepics/')
	def __str__(self):
		return self.fullname