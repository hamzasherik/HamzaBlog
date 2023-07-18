from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    """
    function-based view for listing out posts on the blog application
    """
    post_list = Post.published_manager.all()

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    return render(request, "blogApp/post/list.html", {"post_list": post_list})

def post_detail(request, year, month, day, post):
    """
    function-based view for one particular post and all of its contents
    """
    post = get_object_or_404(Post, published__year=year, published__month=month, published__day=day, slug=post, status=Post.Status.PUBLISHED)

    return render(request, "blogApp/post/detail.html", {"post": post})