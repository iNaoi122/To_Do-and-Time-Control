from django.urls import path
from todo.views import todoView, AddTodoItem, DeleteTodoItem

urlpatterns=[
    path('', todoView , name='To_Do'),
    path('AddTodoItem/', AddTodoItem),
    path('DeleteTodoItem/<int:i>/', DeleteTodoItem),
    ]
