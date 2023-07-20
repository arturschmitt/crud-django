from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task


def index(request):
    
    context = {
        'title':'CRUD Django',
        'tasks':Task.objects.all()
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == "POST":
        Task.objects.create(task_name=request.POST.get("title"), task_desc=request.POST.get("desc")).save()
        return redirect(index)
    return render(request, 'create.html')

def delete(request, id):
    Task.objects.get(id=id).delete()
    return redirect(index)

def update(request, id):
    if request.method == "POST":
        task = Task.objects.get(id = id)
        task.task_name = request.POST.get("title_update")
        task.task_desc = request.POST.get("desc_update")
        task.save()
        return redirect(index)
    context = {
        'title': Task.objects.get(id=id).task_name,
        'desc': Task.objects.get(id=id).task_desc
    }
    return render(request, 'update.html', context)
    