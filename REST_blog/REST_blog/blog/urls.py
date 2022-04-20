from django.urls import path
from django.views import generic

app_name = 'blog'

urlpatterns = (
    path('', generic.TemplateView.as_view(template_name='blog/index.html')),
)
