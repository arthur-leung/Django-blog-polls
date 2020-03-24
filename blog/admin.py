from django.contrib import admin

# Register your models here.
from blog.models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'category', 'author']
    fields = ['title', 'body', 'abstract', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
