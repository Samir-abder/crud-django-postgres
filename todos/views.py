from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from .forms import ProductoForm  # Si estás utilizando un formulario
from django.http import HttpResponseRedirect, JsonResponse
from .models import Producto
from django.core.serializers import serialize


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

def create_producto(request):
    if request.method == 'POST':
        # Si el formulario se envió con datos, procesa los datos del formulario
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Crea una instancia de Producto con los datos del formulario
            producto = form.save()
            # Redirige a alguna página de éxito o muestra un mensaje de éxito
            return HttpResponseRedirect('/success/')
    else:
        # Si el formulario no se envió, crea un formulario vacío
        form = ProductoForm()

'''def getallProducts(request):
    productos = Producto.objects.all()
    productos_serializados = serialize('json', productos)  # Serializa los productos en formato JSON
    return JsonResponse(productos_serializados, safe=False)
    '''

def getallProducts(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})