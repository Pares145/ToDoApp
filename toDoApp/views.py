from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Item, ToDoList
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    todo_lists = request.user.todolist.all().order_by("-added_date")
    return render(request, 'toDoApp/index.html', {"todo_lists": todo_lists})


@login_required(login_url='login')
def details(request, todolist_id):
    todo_list = request.user.todolist.get(id=todolist_id)
    todo_items = todo_list.item_set.all().order_by("-added_date")

    return render(request, 'toDoApp/details.html', {"todo_items": todo_items, "todo_list": todo_list})


@login_required(login_url='login')
def add_todolist(request):

    current_datetime = timezone.now()

    if request.method == "POST":
        new_list = ToDoList(user=request.user, name=request.POST["content"], added_date=current_datetime)
        new_list.save()

        return HttpResponseRedirect("/")

    else:
        return HttpResponse("You cannot add lists this way")


@login_required(login_url='login')
def add_todo(request, todolist_id):

    if request.method == "POST":

        todo_list = request.user.todolist.get(id=todolist_id)
        current_datetime = timezone.now()
        content = request.POST["content"]
        todo_list.item_set.create(added_date=current_datetime, text=content)

        return HttpResponseRedirect("/" + str(todo_list.id))

    else:
        return HttpResponse("You cannot add items this way")


@login_required(login_url='login')
def delete_todolist(request, todolist_id):

    if request.method == "POST":

        todo_list = request.user.todolist.get(id=todolist_id)
        todo_list.delete()

        return HttpResponseRedirect("/")

    else:
        return HttpResponse("You cannot delete lists this way")


@login_required(login_url='login')
def delete_todo(request, todo_id):
    if request.method == "POST":

        item_to_delete = Item.objects.get(id=todo_id)
        todo_lists = request.user.todolist.all()

        if item_to_delete.todolist in todo_lists:
            print("Item deleted")
            item_to_delete.delete()
            return HttpResponseRedirect("/" + str(item_to_delete.todolist.id))

        else:
            return HttpResponse("This item is not in your to do list")

    else:
        return HttpResponse("Item not found/You cannot delete items this way")


@login_required(login_url='login')
def edit_todo(request, todo_id):

    if request.method == "GET":

        to_edit = Item.objects.get(id=todo_id)
        to_do_lists = request.user.todolist.all()

        if to_edit.todolist in to_do_lists:

            todo_items = to_edit.todolist.item_set.all().order_by("-added_date")
            print("Transfer to edit page complete")
            return render(request, 'toDoApp/edit.html',
                          {"todo_items": todo_items, "edit_value": to_edit.text, "todo_id": todo_id,
                           "todolist_id": to_edit.todolist.id})

        else:
            return HttpResponse("This item is not in your to do list/You cannot edit items this way")

    elif request.method == "POST":

        item_to_edit = Item.objects.get(id=todo_id)
        todo_lists = request.user.todolist.all()

        if item_to_edit.todolist in todo_lists:

            item_to_edit.text = request.POST["content"]
            item_to_edit.save()
            print("Item edited")

            return HttpResponseRedirect("/" + str(item_to_edit.todolist.id))

        else:
            return HttpResponse("This item is not in your to do list")
