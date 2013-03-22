from django.contrib import admin
from inspector.models import Phone, Email, Credential, Inspector


class PhoneAdmin(admin.ModelAdmin):
    ''' Admin module for inspector phone model
    '''
    list_display = (
        'pk',
        'phone',
    )


class EmailAdmin(admin.ModelAdmin):
    ''' Admin module for inspector email model
    '''
    list_display = (
        'pk',
        'email',
    )


class CredentialAdmin(admin.ModelAdmin):
    ''' Admin module for inspector credentials model
    '''
    pass


class InspectorAdmin(admin.ModelAdmin):
    ''' Admin module for inspector model
    '''
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'email',
    )


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Credential, CredentialAdmin)
admin.site.register(Inspector, InspectorAdmin)
