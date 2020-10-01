from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text