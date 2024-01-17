from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import *
from .forms import *

def todo(request,pk):
    user = User.objects.get(id=pk)
    todos = Tasks.objects.filter(username=user.id)
    form=TasksForm(initial={'username':user})
    if request.method=="POST":
        form=TasksForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'todolist.html', {'user': user, 'todos': todos,'form':form})

def update_todo(request, pk):
    todo = Tasks.objects.get(id=pk)
    form = TasksForm(instance=todo)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(reverse('todopage', kwargs={'pk': todo.username.id}))
    return render(request, 'update_todo.html', {'form': form})



def delete_todo(request,pk):
    todo = Tasks.objects.get(id=pk)
    form = TasksForm(instance=todo)
    if request.method=='POST':
        todo.delete()
        return redirect(reverse('todopage', kwargs={'pk': todo.username.id}))
    return render(request, 'delete_todo.html', {'form': form})
    
def logout_view(request,pk):
    #could have avoided if I could have used requests module
    logout(request)
    return redirect('home')