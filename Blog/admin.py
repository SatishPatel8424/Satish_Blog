from django.contrib import admin

# Register your models here.

from .models import BlogAuthor, Blog, BlogComment

admin.site.register(BlogAuthor)
admin.site.register(BlogComment)

class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = BlogComment
    max_num=0



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('name', 'author', 'post_date')
    inlines = [BlogCommentsInline]

