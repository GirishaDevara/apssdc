from django.db import models

from django.contrib.auth.models import User


class Details(models.Model):
    vals = [('Male','Male'),('Female','Female')]
    age = models.ImageField(null=True)
    phoneNo = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=vals)
    picture = models.ImageField(upload_to='profilepics/',null=True)
    data_of_birt = models.DateField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.phoneNo