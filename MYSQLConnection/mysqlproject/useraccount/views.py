from django.shortcuts import render
from .forms import UserRegisterForm
from django.http import HttpResponse
from .models import Userregister
from django.core.mail import send_mail
from mysqlproject import settings

def upload(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            name = request.POST['fullname']
            mailid = request.POST['mailid']
            password = name+ "@123"
            model = Userregister(fullname=name,mailid=mailid,image=request.FILES['image'],password=password)
            model.save()
            sub = 'Hi this is gireesha'
            body = 'Welcome to my app,\n this is your user id '+mailid+' and \n password is: '+password
            receiver = request.POST['mailid']
            sender = settings.EMAIL_HOST_USER
            send_mail(sub,body,sender,[receiver])
            return HttpResponse('mail sent')
    form = UserRegisterForm()
    return render(request,'upload.html',{'form':form})


def displayImage(request):
    data = Userregister.objects.all()
    return render(request,'displayImage.html',{"data":data})