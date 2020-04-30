from django.urls import path
from myApp2 import views


urlpatterns=[
    path('',views.hello, name='hello'),
    path('register/',views.register,name='register'),
    path('display/',views.display, name= 'display'),
    path('edit/<int:id>',views.edit,name='edit'),
]