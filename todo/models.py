from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
