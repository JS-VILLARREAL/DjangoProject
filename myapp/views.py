from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateProject

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title   
    })

def hello(request, username):
    return HttpResponse('<h1>Hello, %s</h1>' %username)

def about(request):
    username = 'Steven'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/project.html', {
        'projects': projects
    })

def tasks(request):
    tasks = list(Task.objects.all())
    return render(request, 'tasks/task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_projects(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateProject()
        })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST['name'])
        print(project)
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    task = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': task
    })