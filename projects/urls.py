from django.urls import path
from .views import projectView


urlpatterns = [
     path('', projectView, name="projects"),
]
