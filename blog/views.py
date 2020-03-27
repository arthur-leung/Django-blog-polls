import re

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category, Tag

import markdown


def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def archives(request, year, month):
    post_list = Post.objects.filter(created_at__year=year, created_at__month=month).order_by('-created_at')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def category(request, category_id):
    cate = get_object_or_404(Category, pk=category_id)
    post_list = Post.objects.filter(category=cate).order_by('-created_at')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def tag(request, tag_id):
    tg = get_object_or_404(Tag, pk=tag_id)
    post_list = Post.objects.filter(tags=tg).order_by('-created_at')
    return render(request, 'blog/index.html', context={
        'post_list': post_list,
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={
        'post': post,
    })
