from django.contrib import admin
from appointment.models import Appointment, Feedback, CustomerInformation, InspectionAddress, HouseInformation


# Register your models here.
# DONE - Add preview fields for list view
class AppointmentAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model
    '''
    prepopulated_fields = {'slug': ('full_name',)}
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
    prepopulated_fields = {'slug': ('full_name',)}
    list_display = (
        'full_name',
        'timestamp',
        'email',
        'approve',
    )
    search_fields = ['full_name']


# DONE - Add preview fields for list view
class CustomerInformationAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    list_display = (
        'full_name',
        'phone',
        'mobile',
        'email',
    )
    search_fields = ['full_name']


# DONE - Add preview fields for list view
class InspectionAddressAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('full_name',)}
    list_display = (
        'full_name',
        'inspection_address',
        'inspection_city',
        'inspection_zip',
    )
    search_fields = ['full_name', 'inspection_city', 'inspection_zip']


# DONE - Add preview fields for list view
class HouseInformationAdmin(admin.ModelAdmin):
    ''' Admin for Feedback model
    '''
    prepopulated_fields = {'slug': ('full_name',)}
    list_display = (
        'full_name',
        'address',
        'square_footage',
    )
    search_fields = ['full_name']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(CustomerInformation, CustomerInformationAdmin)
admin.site.register(InspectionAddress, InspectionAddressAdmin)
admin.site.register(HouseInformation, HouseInformationAdmin)
