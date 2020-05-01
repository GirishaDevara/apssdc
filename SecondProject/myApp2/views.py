from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student


def hello(request):
    return HttpResponse('My app 2')


def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print('hi')
        if form.is_valid():
            form.save()
            return redirect('/myapp2/display')
        else:
            return HttpResponse("invalid data")
    form = StudentForm()
    return render(request,'myApp2/register.html',{'form':form})


def display(request):
    data = Student.objects.all()
    # import pdb; pdb.set_trace()
    return render(request,'myApp2/displayStudent.html',{'data':data})

def edit(request,id):
    data = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('display'))
    form = StudentForm(instance=data)
    return render(request,'myApp2/edit.html',{'form':form,'data':data})

def delete(request,id):
    ob = Student.objects.get(id=id)
    if request.method == 'POST':
        ob.delete()
        return redirect(reverse(display))
    return render(request,'myapp2/msg.html',{'info':ob})