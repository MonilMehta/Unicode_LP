from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib.auth import login,authenticate

# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            print(f'succesful {request.user.id}')
            return redirect('todopage',pk=user.id)

    return render(request,'home.html')

def signup(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'Signup.html',{'form':form})
