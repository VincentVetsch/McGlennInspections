from django.contrib import admin
from appointment.models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model '''
    prepopulated_fields = {'slug': ('last_name', 'first_name')}
    list_display = (
        'first_name',
        'last_name',
        'phone',
        'mobile',
        'email',
        'isp_address',
        'isp_city',
        'isp_state',
        'isp_zip',
        'sq_footage',
        'basement',
        'crawlspace',
        'dining_room',
        'living_room',
        'family_room',
        'number_of_bedrooms',
        'number_of_bathrooms',
        'date_req',
        'time_req',
        'notes',
        'timestamp',
    )
    search_fields = ['last_name', 'first_name']

admin.site.register(Appointment, AppointmentAdmin)
