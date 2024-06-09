from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=False, auto_now_add=True)


    def __str__(self) -> str:
        return self.title