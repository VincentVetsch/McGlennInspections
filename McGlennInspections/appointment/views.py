from django.shortcuts import render_to_response
from appointment.models import Appointment


def appointment_page(request):
    '''
        This is the main view for all appointment entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("appointment_page.html", {'appointment': Appointment})


def appointment_page_details(request):
    '''
        This is the detail view for each appointment entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
