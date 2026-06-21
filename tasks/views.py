from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)

    status = request.GET.get('status')
    priority = request.GET.get('priority')

    if status == 'completed':
        tasks = tasks.filter(is_completed=True)
    elif status == 'pending':
        tasks = tasks.filter(is_completed=False)

    if priority:
        tasks = tasks.filter(priority=priority)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})
@login_required

def task_create(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)

            task.owner = request.user

            task.save()

            return redirect('task-list')

    else:

        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})

@login_required

def task_update(request, pk):

    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('task-detail', pk=task.pk)

    else:

        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})

@login_required

def task_delete(request, pk):

    task = get_object_or_404(Task, pk=pk, owner=request.user)

    if request.method == 'POST':

        task.delete()

        return redirect('task-list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})