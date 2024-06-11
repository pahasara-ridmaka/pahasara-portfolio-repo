from django.urls import path
from . import views
from .views import home_page, post_list, PostDetail

urlpatterns = [
    
    path('', home_page, name="home"),
    
    path('posts/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('posts/', post_list, name="posts"),
]
