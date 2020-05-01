from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import UserRegister
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # import pdb;pdb.set_trace()
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = last_name+"123"
            user_name = request.POST.get('user_name')
            mail_id = request.POST.get('user_name')
            phone_number = request.POST.get('user_name')
            age = request.POST.get('age')
            model = UserRegister(first_name=first_name, last_name=last_name, password=password,
                                 user_name=user_name, mail_id=mail_id, phone_number=phone_number, age=age)
            model.save()
            # messages.success(request,'User Details added Successfully')
            return HttpResponse("your password is : "+'/"'+password+'/"')
        else:
            messages.warning(request,'please enter valid details!!')
            return render(request,'register.html',{'form':form})
    form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == "POST":
        data = UserRegister.objects.get(user_name = request.POST['user_name'])
        messages.success(request,'Login successful!! :)')
        return render(request,'details.html',{'data':data})
    return render(request,'login.html',{})