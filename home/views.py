from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from home.forms import PostForm
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts': posts})


def add_post(request):
    if request.method =="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html',{'form': form})

def edit_post(request, post_id=None):
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'blog/post_form.html', {'form': form})