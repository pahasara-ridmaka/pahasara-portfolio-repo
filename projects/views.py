from django.shortcuts import render
from .models import Project

def index(request):
    projects = Project.objects.all().order_by('-date')
    context = { "projects" : projects}
    
    return render(request, 'index.html', context)
