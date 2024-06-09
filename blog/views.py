from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from projects.models import Project


#  - Home Page 
def home_page(request):
    project = Project.objects.all().order_by("-date")
    posts = Post.objects.all()

    context = {"projects" : project, "posts" : posts}

    return render(request, 'index.html', context)


def post_list(request):
    posts = Post.objects.all()
    context = {"posts" : posts}

    return render(request, 'post_list.html', context )