from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
	path('signup/',views.signup,name='signup'),
	path('signin/',auth_views.LoginView.as_view(template_name='userapp/login.html'),name='login'),
	path('home/',views.home,name='home'),
	path('logout/',auth_views.LogoutView.as_view(template_name='userapp/logout.html'),name='logout'),
	path('profile/',views.profile,name='profile'),

]
