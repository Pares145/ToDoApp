from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url='login')
def index(request):
    todo_items = request.user.to_do_items.all().order_by("-added_date")
    return render(request, 'toDoApp/index.html', {"todo_items": todo_items})


@login_required(login_url='login')
def add_todo(request):

    current_datetime = timezone.now()
    content = request.POST["content"]
    request.user.to_do_items.create(user=request.user, added_date=current_datetime, text=content)

    return HttpResponseRedirect("/")


@login_required(login_url='login')
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect("/")


@login_required(login_url='login')
def edit_todo(request, todo_id):

    to_do_to_edit = request.user.to_do_items.get(id=todo_id)

    todo_items = request.user.to_do_items.all().order_by("-added_date")

    return render(request, 'toDoApp/edit.html', {"todo_items": todo_items, "edit_value": to_do_to_edit.text, "todo_id": todo_id})


def update_todo(request, todo_id):
    to_do_to_edit = request.user.to_do_items.get(id=todo_id)
    to_do_to_edit.text = request.POST["content"]
    to_do_to_edit.save()

    return HttpResponseRedirect("/")