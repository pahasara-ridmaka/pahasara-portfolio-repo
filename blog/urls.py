from django.urls import path
from . import views
from .views import home_page, post_list

urlpatterns = [
    
    path('', home_page, name="home"),
    path('posts/', post_list, name="posts"),
]
