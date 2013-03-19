from django.contrib import admin
from navigation.models import Navigation


class NavigationAdmin(admin.ModelAdmin):
    '''
        Admin module for post model
    '''
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

admin.site.register(Navigation, NavigationAdmin)

# Register your models here.
