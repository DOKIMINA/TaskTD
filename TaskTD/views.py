from django.shortcuts import render
from .models import Task, Coment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'