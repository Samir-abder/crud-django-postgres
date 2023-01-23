from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def view_todos(request):
    todos = Todo.objects.all()
    return render(request, 'view_todos.html', {'todos': todos})

def create_todo(request):
    todo = Todo(
        title=request.POST['title'],
        description=request.POST['description'],
    )
    todo.save()
    return redirect('/')

def delete_todo(request, id):
    delete_todo = Todo.objects.get(id=id)
    delete_todo.delete()
    return redirect('/')

def edit_todo(request, id):
    todo = Todo.objects.get(id=id)
    forms = TodoForm(request.POST or None, instance=todo)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('/')
    return render(request, 'edit_todo.html', {'forms': forms})
