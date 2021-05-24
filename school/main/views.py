from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'school/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})
def about(request):
    tasks = Task.objects.order_by('-id')
    answer='не передал'
    if request.method == 'POST':
        answer = 'передал'
    return render(request, 'school/about.html', {'title': 'Страница решения', 'tasks': tasks, 'answer': answer})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Форма была неверная'

    form = TaskForm()
    context = {
        'form': form,
        'error': error

    }
    return render(request, "school/create.html", context)