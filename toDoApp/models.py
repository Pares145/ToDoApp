from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_do_items', null=True)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)