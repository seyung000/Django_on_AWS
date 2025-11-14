from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo
from .form import insert_todo, select_todos

# Create your views here.
def select_todolist(request):

    try:
        if request.method == 'POST':
            todo_name = request.POST.get('task').strip()
            insert_todo(todo_name, request.user)

        return render(request, 'todolist/todo.html',
            {
                'todos': select_todos(request.user) 
            }
        )
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return redirect('select_todolist')
    
def update_todo(request, todo_id):
    try:
        todo = Todo.objects.get(id=todo_id, user=request.user)
        todo.status = not todo.status
        todo.save()
    except Todo.DoesNotExist:
        messages.error(request, 'Todo item not found.')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return redirect('select_todolist')
    

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.delete()

    return redirect('select_todolist')