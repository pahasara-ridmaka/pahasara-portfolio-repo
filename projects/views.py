from django.shortcuts import render
from .models import Project

def projectView(request):
    projects = Project.objects.all().order_by('-date')
    context = { "projects" : projects}
    
    return render(request, 'projects.html', context)
