from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from TaskTD.forms import TaskForm
from .models import Task, Coment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        task_list = Task.objects.filter(author=self.request.user)
        return task_list


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        content = self.request.POST.get('comment')

        if content:
            task.comments.create(author=self.request.user, content=content)
        return redirect('tasks:task_detail', task.id)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    success_url = reverse_lazy('tasks:task_list')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_edit.html'
    success_url = reverse_lazy('tasks:task_list')
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks:task_list')