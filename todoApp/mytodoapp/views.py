from django.shortcuts import render , redirect #redirect is used to redirect user to page after submitting the data
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request): 
	tasks = Todo.objects.all()

	form = TodoForm()

	if request.method == 'POST':
		form = TodoForm(request.POST) #request made by todo form
		if form.is_valid():
			form.save()
		return redirect('/') #redirect to same page

	context = {'tasks': tasks, 'form': form}
	return render(request, 'tasks/list.html', context) #It will render to the list.html file lies on the tasks folder inside templates.