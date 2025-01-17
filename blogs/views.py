from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogs, Post
from .forms import PostForm



def index(request):
    """Home page which shows all blogs """
    blogs = Blogs.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    """Страница показывает все посты для выбранного блога"""
    blog = get_object_or_404(Blogs, id=blog_id) # Получение блога по его ID
    posts = blog.posts.all()
    return render(request, 'blogs/blog_detail.html', {'blog': blog, 'posts': posts})

# Create your views here.
def new_post(request, blog_id):
    """Adding new post"""
    blog = get_object_or_404(Blogs, id=blog_id)

    if request.method !='POST':
        #Empty form
        form = PostForm()
    else:
        # Processing of the sent data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.post = blog
            new_post.save()
            return redirect('blogs:blog_detail', blog_id=blog_id)
        
    context = {'blog': blog, 'form' : form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Editing existing post"""
    post = get_object_or_404(Post, id=post_id)
    blog = post.post

    if request.method !='POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_detail', blog_id = blog.id)
    
    context = {'post':post, 'blog':blog, 'form':form}
    return render(request, 'blogs/edit_post.html', context)

def delete_post(request, post_id):
    """Deleting post"""
    post = get_object_or_404(Post, id=post_id)
    blog = post.post
    post.delete()
    return render('blogd/blog_detail', blog_id=blog.id)

