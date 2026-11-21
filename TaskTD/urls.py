from django.urls import path
from . import views
#from .views import home

app_name = 'tasks'

urlpatterns = [
    #path('', home, name='home')
    path('', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task_detail' ),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit', views.TaskUpdateView.as_view(), name='task_edit'),
    ]