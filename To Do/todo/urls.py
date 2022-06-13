from django.urls import path
from todo.views import TaskList , TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
urlpatterns=[
    path('', TaskList.as_view() , name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name ='task'),
    path('create-task/', TaskCreateView.as_view() , name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view() , name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view() , name='task-delete'),
]
