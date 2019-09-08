from django.shortcuts import render
from django.utils import timezone
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.

def task_list(request):
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.created_date = timezone.now()
            task.save()
            return render(request, 'todo/task_list.html', {'tasks': tasks})
    else:
        form = TaskForm()
    return render(request, 'todo/task_edit.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list', {'tasks': tasks})
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_edit.html', {'form': form})
