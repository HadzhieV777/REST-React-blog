from django.urls import path

from REST_blog.blog_api.views import PostDetail, PostList

app_name = 'blog_api'

urlpatterns = (
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
)
