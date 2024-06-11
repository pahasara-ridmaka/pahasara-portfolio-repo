from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from projects.models import Project
from django.views.generic import DetailView


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

# def post_detail(request):

#     return render(request, 'post_detail.html')

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
