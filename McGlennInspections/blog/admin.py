from django.contrib import admin
from blog.models import Posts


class PostsAdmin(admin.ModelAdmin):
    '''
        Admin module for post model
    '''
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'bodytext', 'timestamp', 'tags')
    search_fields = ['title']

admin.site.register(Posts, PostsAdmin)
