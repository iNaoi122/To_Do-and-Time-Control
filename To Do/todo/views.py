from .models import Task
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks_list.html"

class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
