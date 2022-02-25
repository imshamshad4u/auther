from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('user', views.user,name='user'),
    path('signup', views.usersignup ,name='usersignup'),
    path('patientlogin', views.patientlogin),
    path('doctorlogin',views.doctorlogin)
    # path('signup', views.signup),
]
