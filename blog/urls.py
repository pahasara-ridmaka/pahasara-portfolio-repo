from django.urls import path
from . import views
from .views import home_page, post_list, PostDetail, write, delete_post
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', home_page, name="home"),
    
    path('posts/<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('posts/write/', write, name="write"),
    path('posts/', post_list, name="posts"),
    path('posts/delete/<int:pk>', delete_post, name="delete-post"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name="logout"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)