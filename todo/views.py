from django.shortcuts import render
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.

def task_list(request):
    posts = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/task_list.html', {'tasks': tasks})
