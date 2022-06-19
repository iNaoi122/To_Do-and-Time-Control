from tempfile import template
from .models import Task
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login

# Create your views here.

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()

        search_input = self.request.GET.get("search-area") or ''

        if search_input:
            context["tasks"] = context["tasks"].filter(title__icontains = search_input)

        context["search_input"] = search_input

        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("tasks")
    
class TaskLoginView(LoginView):
        fields = "__all__"
        redirect_authenticated_user = True
        template_name = "todo/login.html"

        def get_success_url(self):
            return reverse_lazy("tasks")

class RegisterUser(FormView):
    template_name = "todo/register.html"
    redirect_authenticated_user = True
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterUser, self).get(*args, **kwargs)
