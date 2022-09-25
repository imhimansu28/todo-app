from gc import get_objects

from django import http
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import *


def login(request):
    return render(request, 'login.html')


# Create your views here.
@login_required
def todoapp(request):
    task = TodoListItem.objects.filter(
        user_id=request.user.id)
    count = task.count()
    context = {'task':  task,  'count': count, }
    return render(request, 'todolist.html', context=context)


def addTodo(request):
    task = request.POST['content']
    date = request.POST['end_date']
    time = request.POST['time']
    new_item = TodoListItem(content=task, end_date=date, time=time)
    new_item.user = request.user
    new_item.save()

    return HttpResponseRedirect('/')


def task_completed(request, task_id):
    is_complete = request.POST['completed']
    if is_complete is 'on':
        is_complete = True
    todo = TodoListItem.objects.filter(id=task_id)
    todo.update(completed=is_complete)
    return HttpResponseRedirect('/')


def deleteTodo(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/')
