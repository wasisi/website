from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post
def post_list(request):
    posts = Post.published.all() # uses the manager that was created in models
    return render(request,
                 'blog/list.html',
                 {'posts': posts})

# Second view to display single post
def post_detail(request, year, month, day, post):
	post = get_object_or_404(post, slug =post,
									status =published,
									publish__year=year,
									publish__month=month,
									publish__day=day)
	return render(request,
				'blog/detail.html',
				{'post': post})
