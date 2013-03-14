from django.contrib import admin
from cust_feedback.models import Feedback


# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    '''
        Admin module for appointment model
    '''
    prepopulated_fields = {'slug': ('last_name', 'first_name',)}
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
        'comments',
        'timestamp',
    )
    search_fields = ['last_name', 'first_name']

admin.site.register(Feedback, FeedbackAdmin)
