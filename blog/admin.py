from django.contrib import admin
from .models import Tag, Category, Post, Comment, Reply, Image

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Image)

