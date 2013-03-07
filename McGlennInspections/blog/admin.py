from django.contrib import admin
from blog.models import Post
# Register your models here. from beer.models import Beer, Brewery


class PostAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('title',)}
        list_display = ('title', 'author', 'bodytext', 'timestamp')
        search_fields = ['title']

admin.site.register(Post, PostAdmin)
