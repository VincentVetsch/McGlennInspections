from django.contrib import admin
from rvalues.models import RValue


# Register your models here.
class RValueAdmin(admin.ModelAdmin):
    ''' Admin module for Rvalues model '''
    prepopulated_fields = {'slug': ('title',)}
    #TODO - Add proper fields
    list_display = ('title', 'author', 'bodytext', 'timestamp')
    search_fields = ['title']

admin.site.register(RValue, RValueAdmin)
