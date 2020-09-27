from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Todo


def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'toDoApp/index.html', {"todo_items": todo_items})


def add_todo(request):

    current_datetime = timezone.now()
    content = request.POST["content"]
    created_object = Todo.objects.create(added_date=current_datetime, text=content)
    length_of_todos = Todo.objects.all().count()

    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("/")
