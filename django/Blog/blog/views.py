from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def intro(request):
	return render(request, 'blog/into.html',{})

def work(request):
	return render(request, 'blog/work.html',{})

def hobby(request):
	return render(request, 'blog/hobby.html',{})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})