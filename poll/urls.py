from django.urls import path
from . import views

urlpatterns=[
    path('open/',views.open,name='open'),
    path('loginUser/',views.loginUser,name='loginUser'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
            ]