from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('tasks/new/', views.task_create, name='task-create'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task-update'),
    path('tasks/<int:pk>/delete', views.task_delete, name='task-delete'),
]