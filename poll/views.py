from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
import requests
# Create your views here.
from .models import Adminl
from .models import SignUp

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def open(request):
    return render(request,'login.html')
'''
ef logi(request):
    l=Adminl.objects.all()
    print(l[0].admin_id)
    if request.method=="POST":
        print(l[0].password)
        admin_id=request.POST.get('admin_id')
        password=request.POST.get('password')
        print(admin_id)
        print(l[0].admin_id)
        if ((int(admin_id)==int(l[0].admin_id)) and (str(password)==str(l[0].password))):
            print("hii")
            return render(request,'homepage.html')
        else:
            content={"message":"Invalid Credentials"}
            return render(request,'login.html',content)

def loginpage(request):
    if request.method=='POST':
        admin_id=request.POST.get('admin_id')
        password=request.POST.get('password')

        user=authenticate(request,admin_id=admin_id,password=str(password))

        if user is not None:
            login(request,user)
            return render(request,'homepage.html')'''

def loginUser(request):
    if request.method=='POST':
        uname=request.POST.get("uname")
        psw=request.POST.get("psw")
        print("hlo")
        user=authenticate(request,uname=uname,psw=psw)
        print("hii")
        if user is not None:
            print("hey")
            login(request,user)
            return render(request,'homepage.html')
        else:
            messages.info(request,"Invalid Credentials")

    else:
        context={}
        return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginpage')

def home(request):
    return render(request,'homepage.html')