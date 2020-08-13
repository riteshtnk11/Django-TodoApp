# redirect is used to redirect user to page after submitting the data
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.


def index(request):
    tasks = Todo.objects.all()  # Get all data of the todo table

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)  # request made by todo form
        if form.is_valid():
            form.save()
        return redirect('/')  # redirect to same page

    context = {'tasks': tasks, 'form': form}
    # It will render to the list.html file lies on the tasks folder inside templates.
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Todo.objects.get(id=pk)

    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, 'tasks/edit_task.html', context)


def deleteTask(request, pk):
    task = Todo.objects.get(id=pk)

    if request.method == 'POST':
    	task.delete()
    	return redirect('/')

    context = {'item': task}
    return render(request, 'tasks/delete_task.html', context)
