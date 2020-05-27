from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from portal_user_account import settings


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, 'Log in successful')
            return render(request, 'welcome.html')
        elif not User.objects.filter(username=username):
            # here user does not exists
            temp_password = 'abc@1234'
            user = User.objects.create_user(username=username, email=username, password=temp_password)
            user.save()
            sub = 'Activate account'
            body = 'Welcome to our portal,\nthis is your user id ' + username + ' and \npassword : ' + \
                   temp_password+" \nReset your password here http://127.0.0.1:8000/resetpswd"
            receiver = username
            sender = settings.EMAIL_HOST_USER
            send_mail(sub, body, sender, [receiver])
            return HttpResponse('user added')
        else:
            return HttpResponse('password')
    else:
        return render(request, 'login.html')

def reset(request):

    return render(request,'ResetPassword.html')