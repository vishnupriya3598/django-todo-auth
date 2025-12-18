from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from .models import Task
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        task_time = request.POST.get("task_time")

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                task_time=task_time if task_time else None
            )
        return redirect("todo")

    tasks = Task.objects.filter(user=request.user)
    return render(request, "todo.html", {"tasks": tasks})
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("todo")
    
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.task_time = request.POST.get("task_time") or None
        task.completed = True if request.POST.get("completed") == "on" else False
        task.save()
        return redirect("todo")

    return render(request, "edit_task.html", {"task": task})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect("todo")

