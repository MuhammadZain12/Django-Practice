from django.shortcuts import render,redirect
from myApp.forms import UserForm,UserProfileForm

# For Login view

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


# Create your views here.

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))


@login_required
def welcome(request,name):
  return render(request,'myApp/welcome.html',{'name':name})

def index(request):
  return render(request,'myApp/index.html')

def home(request):
  my_dict={
    'var':'Home Page',
    'name':'muhammad zain',
    'institute':'University Of Engineering and Technology',
    'status':0
  }
  return render(request,'myApp/home.html',my_dict)


def user_login(request):
  if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user:
      if user.is_active:
        login(request,user)
        return HttpResponseRedirect(reverse("welcome",args=[username]))
      else:
        return HttpResponse("Your account is no more active")  
    else:
      print(f"Some one tried to login with Username : {username} Password : {password}")
      return HttpResponse("Your given data is not correct")
  else:
    return render(request,'myApp/sign_in.html',{})






def sign_up(request):
  done=False
  if request.method=='POST':
    print(request.POST)
    form=UserForm(request.POST)   
    form2=UserProfileForm(request.POST)
    if form.is_valid() and form2.is_valid():
      user=form.save()
      user.set_password(user.password)
      user.save()
      profile=form2.save(commit=False)
      profile.user=user
      if 'profile_image' in request.FILES:
        profile.profile_image=request.FILES['profile_image']
      profile.save()
      done=True
    else:
      print(form.errors,form2.errors)
  else:
    form=UserForm()
    form2=UserProfileForm()
  return render(request,'myApp/sign_up.html',{'basic_info':form,'extra_info':form2,'registered':done})   
        

def other(request):
  return render(request,'myApp/other.html')    
