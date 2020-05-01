from django import forms
from .models import UserRegister


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegister
        # fields = "__all__"
        fields = ['first_name','last_name',
                  'user_name','mail_id','phone_number' ]
