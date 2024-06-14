from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Post
from projects.models import Project
from django.views.generic import DetailView

from django.contrib.auth import logout



# froms 
from .forms import WriteForm

from django.contrib.auth import views as auth_views

# - auth decorators
from django.contrib.auth.decorators import login_required



#  - Home Page 
def home_page(request):
    project = Project.objects.all().order_by("-date")
    posts = Post.objects.all()
    user = request.user;

    context = {"projects" : project, "posts" : posts, "user": user}

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


# - delete post

def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    
    if request.user == post.author:
        post.delete()

    return redirect('posts')

# - Write an Aritle

@login_required(login_url = 'login')
def write(request):

    form = WriteForm()

    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)

        if form.is_valid() :
            form.save()

            return redirect('posts')
        
    context = {"form": form}

    return render(request, 'write.html', context)


# # - custom login view
# class CustomLoginView(auth_views.LoginView):
#     def get_success_url(self) -> str:
#         custom_success_url = reverse_lazy('posts')
#         return custom_success_url