from django.shortcuts import render,redirect ,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required



# Create your views here.
def inscription(request):
    if request.method=='POST':

        form= New_userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = New_userForm()
    return render(request,'profil/inscription.html',locals())

def index(request):
    coureu=Coureur.objects.all()
    compet= Competition.objects.all()
    
    return render(request,'index.html', {'competit':compet,'coureur':coureu})

def login(request):
    error=False
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user= authenticate(username=username,password=password)
            if user:
                login(request, user)
                return redirect('accueil')
            else:
                error=True

    else:
        form=LoginForm()
    return render(request,'profil/connection.html',{'form':form})

def deconnection(request):
    logout(request)
    return redirect('accueil')
@login_required
def profil(request):
    return render(request,'profil/profil.html')

def course(request):

    return render(request,'course.html')