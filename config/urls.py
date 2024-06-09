
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
    path('', include('blog.urls')),
]
