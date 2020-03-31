from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from blog.models import Post
from comments.forms import CommentForm


@require_POST
def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        return redirect(post)

    context = {
        'post': post,
        'form': form,
    }
    print(context)
    return render(request, 'comments/preview.html', context=context)

