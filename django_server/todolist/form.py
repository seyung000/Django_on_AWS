from .models import Todo
from user.models import CustomUser

def insert_todo(todo_name, user):
    todo = Todo.objects.filter(todo_name=todo_name, user=user)

    if todo:
        raise ValueError("Todo with this name already exists for the user.")
    new_todo = Todo(todo_name=todo_name, user=user)
    new_todo.save()


def select_todos(user:CustomUser) -> list:
    return Todo.objects.filter(user=user)


def get_todo(user:CustomUser, todo_id:int) -> list:
    try:
        return Todo.objects.get(id=todo_id, user=user)
    except Todo.DoesNotExist:
        raise ValueError("Todo item not found.")