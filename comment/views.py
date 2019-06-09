from django.contrib import messages
# from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView
#
from project.decorators import profile_required
from .models import Comment
from .forms import CommentForm


def comment_list(request):
    queryset = Comment.objects.all()
    context = {
        'comment_list': queryset
    }
    return render(request, "comment/list.html", context)


def comment_detail(request, id):
    comment = get_object_or_404(Comment, id=id)
    context = {
        'comment': comment
    }
    return render(request, "comment/detail.html", context)


@profile_required
def create_comment(request):
    form = CommentForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user.profile
                comment.save()
                return redirect('comment-list')
    else:
        messages.info(request, 'Войдите в свой аккаунт')
        return redirect('login-page')
    return render(request, "comment/create_comment.html", locals())


def update_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    form = CommentForm(request.POST or None, instance=comment)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(comment.get_absolute_url())
    return render(request, "comment/update_comment.html", locals())


def confirm_delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    return render(request, "comment/delete_comment.html", locals())


def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    messages.info(request, 'Комментарий удален')
    return redirect("comment-list")
