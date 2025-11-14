from django.urls import path
from .views import select_todolist, update_todo, delete_todo

urlpatterns = [
    # http://localhost:8000/
    path('', select_todolist, name='select_todolist'),
    path('update/<int:todo_id>/', update_todo, name='update-task'),
    path('delete/<int:todo_id>/', delete_todo, name='delete-task'),
]
