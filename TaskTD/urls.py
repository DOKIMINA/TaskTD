from django.urls import path
from . import views
#from .views import home
from django.contrib.auth.views import LogoutView
app_name = 'tasks'

urlpatterns = [
    #path('', home, name='home')
    path('', views.TaskListView.as_view(), name='task_list'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='tasks:login'), name='logout'),
    
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task_detail' ),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/edit', views.TaskUpdateView.as_view(), name='task_edit'),
    ]