from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/<int:todolist_id>/', views.add_todo, name='add_todo'),
    path('add_todolist/', views.add_todolist, name='add_todolist'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('delete_todolist/<int:todolist_id>/', views.delete_todolist, name='delete_todolist'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('<int:todolist_id>', views.details, name='todolist'),
]