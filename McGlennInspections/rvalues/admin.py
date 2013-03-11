from django.contrib import admin
from rvalues.models import RValue


# Register your models here.
class RValueAdmin(admin.ModelAdmin):
    ''' Admin module for Rvalues model '''
    prepopulated_fields = {'slug': ('material',)}
    list_display = (
        'material',
        'r_value',
        'density',
        'timestamp',
        'perm',
        'absorbtion',
        'flamespread',
        'smoke',
        'toxicity',
        'agingeffect',
        'timestamp',
    )
    search_fields = ['material']

admin.site.register(RValue, RValueAdmin)
