from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from portal_user_account import settings
import uuid


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            messages.success(request, 'Log in successful')
            return render(request, 'welcome.html')
        elif not User.objects.filter(username=username):
            # here user does not exists
            temp_password = str(uuid.uuid4().fields[-1])[:7]
            user = User.objects.create_user(username=username, email=username, password=temp_password)
            user.save()
            id_ = user.id
            sub = 'Activate account'
            body = 'Welcome to our portal,\nthis is your user id ' + username + ' and \npassword : ' + \
                   temp_password + '-' + str(id_) + " \nReset your password here http://127.0.0.1:8000/resetpswd"
            receiver = username
            sender = settings.EMAIL_HOST_USER
            send_mail(sub, body, sender, [receiver])
            return HttpResponse('user added')
        else:
            messages.error(request, 'invalid mail or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def reset(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new = request.POST.get('password1')
        confirm = request.POST.get('password1')
        if new == confirm:
            user = User.objects.get(id=old_password.split('-')[-1])
            user.set_password(new)
            user.save()
            return redirect('login')
    return render(request, 'ResetPassword.html')
