from django.contrib import admin
from appointment.models import Appointment, Feedback, CustomerInformation, InspectionAddress


# TODO - Research howto make Admin classes more user friendly.  And
# how to give more detailed information.
# DONE - Add preview fields for list view
class AppointmentAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model
    '''
    prepopulated_fields = {'slug': ('date_requested',)}
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
    prepopulated_fields = {'slug': ('email',)}
    list_display = (
        'email',
        'timestamp',
        'approve',
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
    prepopulated_fields = {'slug': ('inspection_city',)}
    list_display = (
        'inspection_address',
        'inspection_city',
        'inspection_zip',
    )
    search_fields = ['full_name', 'inspection_city', 'inspection_zip']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(CustomerInformation, CustomerInformationAdmin)
admin.site.register(InspectionAddress, InspectionAddressAdmin)
