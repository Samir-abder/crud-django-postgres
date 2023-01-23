from django.urls import path
from .views import view_todos, create_todo, delete_todo, edit_todo

urlpatterns = [
    path('', view_todos, name="todos"),
    path('new_todo/', create_todo, name="create_todo"),
    path('delete_todo/<int:id>', delete_todo, name="delete_todo"),
    path('edit_todo/<int:id>', edit_todo, name="edit_todo"),
]
