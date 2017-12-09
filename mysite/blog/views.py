from django.shortcuts import render

from blog.models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'object_list': posts})

