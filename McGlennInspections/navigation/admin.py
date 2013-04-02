from django.contrib import admin
from navigation.models import Navigation


class NavigationAdmin(admin.ModelAdmin):
    '''
        Admin module for post model
    '''
    prepopulated_fields = {'slug': ('title',),
                           'div_class': ('slug', 'parent')}
    list_display = (
        'title',
        'link',
        'type_of_link',
        'parent',
        'div_class',
    )

    search_fields = ['title']

admin.site.register(Navigation, NavigationAdmin)

# Register your models here.
