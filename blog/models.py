from django.db import models
from django.conf import settings

# Create your models here.
class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    photo = models.ImageField('画像', blank=True)
    title = models.CharField('タイトル', max_length=32)
    text = models.TextField('本文')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='カテゴリ')

    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='投稿者')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField('お名前', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    target = models.ForeignKey(Post, on_delete=models.PROTECT, verbose_name='どの記事へのコメントか')

    def __str__(self):
        return self.text

class Reply(models.Model):
    name = models.CharField('お名前', max_length=255)
    text = models.TextField('本文')
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    target = models.ForeignKey(Comment, on_delete=models.PROTECT)

    def __str__(self):
        return self.text

class Image(models.Model):
    title = models.CharField(max_length=255,blank=True)
    photo = models.ImageField('画像', blank=True)
    def __str__(self):
        return self.title        
