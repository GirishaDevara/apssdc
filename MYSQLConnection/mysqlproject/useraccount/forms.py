from django.forms import ModelForm
from .models import Userregister

class UserRegisterForm(ModelForm):
    class Meta:
        model = Userregister
        fields = ['fullname', 'mailid', 'image']