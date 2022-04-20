
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('REST_blog.blog.urls', namespace='blog')),
    path('api/', include('REST_blog.blog_api.urls', namespace='blog_api')),
]
