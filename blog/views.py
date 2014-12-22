from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})