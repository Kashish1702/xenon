from django.shortcuts import render , HttpResponse ,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pwd=request.POST.get('password1')
        pc=request.POST.get('password2')
        if pwd!=pc:
            return HttpResponse("Password not match")
        else:
           my_user=User.objects.create_user(uname,email,pwd)
           my_user.save()
           return redirect('login')
        
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pas=request.POST.get('pass')
        user=authenticate(request,username=username,password=pas)
        if user is not None:
            login(request,user)
            return redirect('contactus')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')
def Contactus(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        email=request.POST.get('email')
        mssg=request.POST.get('message')
        return HttpResponse("Form submitted successfully")
    return render(request,'contactus.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')