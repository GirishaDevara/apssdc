from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student


def hello(request):
    return HttpResponse('My app 2')


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        return redirect(register)
    form = StudentForm()
    return render(request,'myApp2/register.html',{'form':form})


def display(request):
    data = Student.objects.all()
    # import pdb; pdb.set_trace()
    return render(request,'myApp2/displayStudent.html',{'data':data})