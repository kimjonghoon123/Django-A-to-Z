from django.shortcuts import render
from .models import post


def index(request):
    posts = post.objects.all().order_by('-pk')


    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
