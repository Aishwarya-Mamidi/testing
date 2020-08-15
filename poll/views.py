from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse
import requests
# Create your views here.
from .models import Adminl
from .models import SignUp
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def open(request):
    return render(request,'reg.html')
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
        uname=request.POST['uname']
        psw=request.POST['psw']
        print("hlo")
        user=authenticate(request,uname=uname,psw=psw)
        print("hii")

        if user is not None:
            print("hey")
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('loginUser')

    else:
        context={}
        return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def home(request):
    return render(request,'homepage.html')

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'reg.html',{'form':form})