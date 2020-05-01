from django.db import models


class UserRegister(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    mail_id = models.EmailField()
    phone_number = models.CharField(max_length=12)
    age = models.IntegerField()
    def __str__(self):
        return self.user_name
