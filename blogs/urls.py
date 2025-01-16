from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),  #main page
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'), #page of specific blog
]
