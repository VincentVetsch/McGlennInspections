from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    ''' Admin module for post model '''
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'bodytext', 'timestamp')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
