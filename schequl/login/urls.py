from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('regform', views.regform, name='regform'),
    path('login', views.login, name='login'),
    path('forgot', views.forgot, name='forgot'),
    path('registration', views.registration, name='registration'),
    path('logout', views.logout, name='logout')
]
