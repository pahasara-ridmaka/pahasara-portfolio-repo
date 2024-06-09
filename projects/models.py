from django.db import models

class Project(models.Model):
    date = models.DateField( auto_now=False, auto_now_add=False)
    title = models.CharField( max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField("projects.Tag")


    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # def get_display_name(self):
    #     return self.name


    def __str__(self):
        return self.name
    