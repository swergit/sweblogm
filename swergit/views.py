from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
def home(request):
     context = {}
     return render(request, 'swergit/home.html', context)

def contact(request):
     context = {}
     return render(request, 'swergit/contact.html', context)

def about(request):
      context = {}
      return render(request, 'swergit/about.html', context)


def main(request):
      context = {}
      return render(request, 'swergit/main.html', context)


def post_list(request):
    context = {}
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'swergit/blog.html', {'posts': posts})

def actual_post(request, pk):
      context = {}
      post = Post.objects.get(id=pk)
      posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
      return render(request, 'swergit/blogpost.html', {'post': post})

