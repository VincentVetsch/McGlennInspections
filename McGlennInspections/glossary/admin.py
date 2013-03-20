from django.contrib import admin
from glossary.models import Term
# Register your models here.


class TermAdmin(admin.ModelAdmin):
    ''' Admin module for terms model '''
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'definition')
    search_fields = ['title']

admin.site.register(Term, TermAdmin)
