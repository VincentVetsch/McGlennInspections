from django.contrib import admin
from pages.models import HomePage


class TinyMCEAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', '/media/js/tiny_mce/textareas.js',)

admin.site.register(HomePage)
