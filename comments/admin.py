from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_at']
    fields = ['name', 'email', 'url', 'text', 'post']


admin.site.register(Comment, CommentAdmin)
