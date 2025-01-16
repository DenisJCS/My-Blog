from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.

def index(request):
    """Home page which shows all blogs """
    blogs = Blogs.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    """Page shows all posts for choosen blog"""
    blog = get_object_or_404 (Blogs, id=blog_id) #Getting blog by it's id
    posts = blog.post_set.all()
    return  render(request, 'blogs/blog_detailed.html', {'blog':blog, 'posts':posts})
