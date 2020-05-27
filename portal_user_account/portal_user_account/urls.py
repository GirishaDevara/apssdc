from django.contrib import admin
from django.urls import path
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('reset/',views.reset, name='reset')
]
