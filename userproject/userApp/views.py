from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Register


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse("Registration successfull")
    form = RegisterForm()
    return render(request,'userApp/register.html',{'form':form})


def display(request):
    data = Register.objects.all()
    print(data)
    return render(request,'userApp/display.html',{'data':data})