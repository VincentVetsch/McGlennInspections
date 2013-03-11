from django.contrib import admin
from slideshow.models import Slide


# Register your models here.
class SlideAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model '''
    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'author',
        'title',
        'bodytext',
        'image',
        'timestamp',
    )
    search_fields = ['title']

admin.site.register(Slide, SlideAdmin)
