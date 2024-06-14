from typing import Iterable
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    title = models.CharField( max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    thumbnail = models.ImageField( upload_to="uploads/", max_length=100, default="")
    #comments - later will add


    def __str__(self) -> str:
        return self.title