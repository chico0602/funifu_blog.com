from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Comment, Category, Tag
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

class PostCategoryList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return super().get_queryset().filter(category=category)

class PostTagList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return super().get_queryset().filter(tags=tag)
