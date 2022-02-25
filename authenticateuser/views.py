from ssl import HAS_TLSv1_1
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request ,'home.html')

def user(request):
    usertext=request.POST.get('usertype','default')
    print(usertext)
    if usertext=='doctor':
        return render (request,'doctor.html')
    else:
        return render (request,'patient.html')


def usersignup(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        profile=request.POST['profilepic']
        user_name=request.POST['username']
        email_signup=request.POST['emailsignup']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']
        address=request.POST['address']
        

        if password!=confirm_password:
            return HttpResponse("passwords did not match, please signup again")
        myuser=User.objects.create_user(user_name,email_signup,password)
        myuser.fname=first_name
        myuser.lname=last_name
        myuser.add=address
        myuser.save()
        return  redirect('user')
        # return  HttpResponse("Account created successfully!")

        
    else:
        return HttpResponse('page-not found')


def patientlogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        

        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            params={'Patientusername':loginusername,'Patientpassword':loginpass}
            return render(request,'patientlogin.html',params)

def doctorlogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user=authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request,user)
            params={'Doctorusername':loginusername,'Doctorpassword':loginpass}
            return render(request,'doctorlogin.html',params)
