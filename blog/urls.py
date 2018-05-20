
from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<slug>', views.blog_detail, name="detail"),
]