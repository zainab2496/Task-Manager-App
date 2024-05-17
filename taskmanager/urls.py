# taskmanager/urls.py

from django.urls import path
from taskmanager import views

urlpatterns = [
    path("", views.home, name='home'),
    path('taskmanager', views.task_list, name='task_list'),
    path('taskmanager/<int:pk>/', views.task_detail, name='task_detail'),
    path('taskmanager/new/', views.task_create, name='task_create'),
    path('taskmanager/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('taskmanager/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
