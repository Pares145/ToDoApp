from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:todo_id>/', views.edit_todo, name='edit_todo'),
    path('edit_todo/<int:todo_id>/update_todo/', views.update_todo, name='update_todo'),

]