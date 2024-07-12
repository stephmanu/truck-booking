from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    


class User(models.Model):
    userid = models.AutoField(('userid'), primary_key=True)
    username = models.CharField(('username'), max_length=128, null=False, blank=False, unique=True)
    email = models.EmailField(("email"), max_length=254, unique=True)
    password = models.CharField(('password'), max_length=128, null=False, blank=False, unique=True)

    
    def __str__(self):
        return self.body[0:50]