from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import CommentCreateForm

# Create your views here.
class PostList(generic.ListView):
    model = Post
    ordering = '-created_at'

class PostDetail(generic.DetailView):
    model = Post

class CommentCreate(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_pk)
        comment = form.save(commit=False)
        comment.target = post
        comment.save()
        return redirect('blog:post_detail', pk=post_pk)
