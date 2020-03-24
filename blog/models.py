import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


class Category(models.Model):
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    abstract = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    created_at = models.DateTimeField('创建时间', default=timezone.now)
    updated_at = models.DateTimeField('更新时间')

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.abstract = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
