from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import UserRegister


# Create your views here.
def register(request):
    if request.method == "POST":
        pass
    form = UserRegisterForm()
    return render(request,'register.html',{'form':form})