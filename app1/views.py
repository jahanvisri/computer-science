from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def indexpage(request):
    return render(request, 'index.html')


def loginpage(request):
    if request.method=='POST':     
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       #print(username,pass1) 
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
            login(request,user)
            return redirect('index')
       else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'login.html')



def signuppage(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1')
       pass2=request.POST.get('password2')

       if pass1!=pass2:
            return HttpResponse("Password mismatch")
       else:
             my_user=User.objects.create_user(uname,email,pass1,)
             my_user.save()
             return redirect('login')
    return render(request, 'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('login')