from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hi(request):
	return HttpResponse("<h2>Welcome to django</h2>")

def hello(request,name):
	return HttpResponse("<h3>Welcome to django Session</h3>"+name)

def rollno(reg,id):
	txt='<h2>your rollno is {} <h2>'.format(id)
	return HttpResponse(txt)
def message(request):
	return render(request,'firstApp/message.html',{})

def register(request):
	if request.method=='POST':
		name=request.POST['username']
		mobileno=request.POST['mobilenum']
		email=request.POST['email']
		#print(name)
		return HttpResponse("Done successfully")
	return render(request,'firstApp/signup.html',{})

def details(request):
	data={'name':"Ranga",'RollNum':"4a2"}
	return render(request,'firstApp/details.html',{'data':data})


