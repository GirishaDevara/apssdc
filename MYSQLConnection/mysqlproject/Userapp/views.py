from django.shortcuts import render
from .forms import Usersignupform
from django.http import HttpResponse
from django.contrib.auth.models import User


def signup(request):
	if request.method == "POST":
		form=Usersignupform(request.POST)
		# import pdb; pdb.set_trace()
		# print(form.is_valid())
		if form.is_valid():
			form.save()
			return HttpResponse('Done')
	form = Usersignupform()
	return render(request, 'userapp/signup.html', {'form': form})


def home(request):
	return render(request,'userapp/home.html',{})


def profile(request):
	#form=User.objects.get()
	return render(request,'userapp/profile.html',{})