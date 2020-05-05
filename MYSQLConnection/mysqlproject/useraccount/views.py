from django.shortcuts import render
from .forms import UserRegisterForm
from django.http import HttpResponse
from .models import Userregister

def upload(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponse('Image uploaded.')
    form = UserRegisterForm()
    return render(request,'upload.html',{'form':form})


def displayImage(request):
    data = Userregister.objects.all()
    return render(request,'displayImage.html',{"data":data})