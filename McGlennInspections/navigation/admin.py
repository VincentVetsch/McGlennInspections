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
        'admin_flag',
        'order_in_list',
        'link',
        'type_of_link',
        'parent',
        'div_class',
    )
    list_filter = ['admin_flag', 'parent', 'type_of_link']
    search_fields = ['title', 'parent']

admin.site.register(Navigation, NavigationAdmin)

# Register your models here.
