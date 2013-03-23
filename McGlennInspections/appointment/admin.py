from django.contrib import admin
from appointment.models import Appointment, Feedback, CustomerName, InspectionAddress, CustomerEmail, CustomerPhone


# DONE - Research howto make Admin classes more user friendly.  And
# how to give more detailed information.
# DONE - Add preview fields for list view
class AppointmentAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model
    '''
    #prepopulated_fields = {'slug': ('full_name',)}
    list_display = (
        'full_name',
        'date_requested',
        'time_requested',
        'timestamp',
    )
    search_fields = ['full_name']


# DONE - Add preview fields for list view
class FeedbackAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('customer',)}
    list_display = (
        'customer',
        'timestamp',
        'approved',
    )


# DONE - Add preview fields for list view
class CustomerInformationAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'mobile',
        'email',
    )
    search_fields = ['first_name', 'last_name']


# DONE - Add preview fields for list view
class InspectionAddressAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('inspection_address',)}
    list_display = (
        'name',
        'inspection_address',
        'inspection_city',
        'inspection_zip',
    )
    search_fields = ['full_name', 'inspection_city', 'inspection_zip']


class CustomerNameAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    list_display = (
        'first_name',
        'last_name',
    )


class CustomerEmailAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('email',)}
    list_display = (
        'name',
        'email',
        'email_type',
    )


class CustomerPhoneAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('phone',)}
    list_display = (
        'name',
        'phone',
        'phone_type',
    )


class InspectorNotesAdmin(admin.ModelAdmin):
    ''' Admin for Inspector Notes
    '''
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'name',
    )


admin.site.register(CustomerPhone, CustomerPhoneAdmin)
admin.site.register(CustomerEmail, CustomerEmailAdmin)
admin.site.register(CustomerName, CustomerNameAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(InspectionAddress, InspectionAddressAdmin)
