from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),  #main page
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('new_post/<int:blog_id>/', views.new_post, name = 'new_post'),
    path('edit_post/<int:blog_id>', views.edit_post, name = 'edit_post'),
    path('delete_post/<int:blog_id>/', views.delete_post, name = 'delete.post'),
]
