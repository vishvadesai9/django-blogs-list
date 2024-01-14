from django.shortcuts import render, get_object_or_404
from blogs_app.models import BlogPost

def index(request):
    return render(request, 'index.html')

def detail(request, post_id):
    blog_post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_detail.html', {'blog_post': blog_post})