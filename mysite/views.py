from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from slider.models import Slider

def home(request):
    slider = Slider.objects.all()
    data = {
        'slider':slider
    }
    return render (request,'index.html',data)

def account(request):
    if request.method == "POST":
        email_or_username = request.POST.get('email_or_username')
        password = request.POST.get('password')

        user = None

        try:
            user_obj = User.objects.get(email = email_or_username)
            user = authenticate(request,username = user_obj.username,password = password)
        except User.DoesNotExist:
            user = authenticate(request,username = email_or_username , password = password)


        if user is not None:
            login (request,user)
            messages.success (request,"Login Sucessfully.......!")
            return redirect ('home')
        else:
            messages.error (request,"There was a error.Plz Try Again.......!")
            return redirect ('home')    




    return render (request,'account.html')


def logout_as(request):
    logout(request,)
    messages.success(request,"Logout Successfully.....!")
    return redirect ('account')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')


        if password != password1:
            messages.success (request,"Password Doesnt Match.....!")
            return redirect ('account')

        if User.objects.filter(email= email).exists():
            messages.success (request,"Email is already Taken.....!")
            return redirect ('account')

        if User.objects.filter(username= username).exists():
                messages.success (request,"Username is already Taken.....!")
                return redirect ('account')


        user = User.objects.create_user(email=email , username=username , password=password)

        messages.success (request,"Account Register Successfully........!")          

        return redirect ('account')  













