from django import forms
from .models import Todo
from .models import Producto

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'