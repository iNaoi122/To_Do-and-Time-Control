from http.client import HTTPResponse
from django.shortcuts import render
from .models import TodoList
from django.http import HttpResponseRedirect

# Create your views here.

def todoView(request):
    all_todo_item = TodoList.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_item})

def AddTodoItem(request):
    new_item = TodoList(content = request.POST["content"])
    new_item.save()
    return HttpResponseRedirect('/')

def DeleteTodoItem(request, i):
    TodoList.objects.get(id = i).delete()
    return HttpResponseRedirect('/')

