from django.contrib import admin
from appointment.models import Appointment
# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    ''' Admin module for appointment model '''
    prepopulated_fields = {'slug': ('title',)}
    #TODO - Add proper fields
    list_display = ('title', 'author', 'bodytext', 'timestamp')
    search_fields = ['title']

admin.site.register(Appointment, AppointmentAdmin)
