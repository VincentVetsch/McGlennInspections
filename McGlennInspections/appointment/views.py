from django.shortcuts import render_to_response
from django.template import RequestContext
from appointment.models import Appointment
from McGlennInspections.settings import SITENAME


def appointment(request):
    ''' appointment:  This is the main view for all appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Insure that this page is only available to admin users
    # TODO - Start adding the content to the page
    entries = Appointment.objects.order_by('-timestamp')
    # TODO - Add basic CustomerInformation
    content = {'appointment': entries,
               'site': SITENAME,
              }
    return render_to_response(
        "appointment.html",
        content,
        context_instance=RequestContext(request)
    )


def appointment_change_status(request):
    ''' appointment_change_status:  This is the view to change the status of the
                       appointment_page.

    Arguments:
        request
    Return:
        Returns the render_to_response function
    '''
    # TODO - work on passing the object selected
    entry = Appointment.objects.all()
    content = {'appointment': entry,
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_change_status.html',
        content,
        context_instance=RequestContext(request)
    )


def appointment_add_inspector(request):
    ''' appointment_add_inspector:  This is the view to add an inspector to the
                       appointment.

    Arguments:
        request
    Return:
        Returns the render_to_response function
    '''
    # TODO - work on passing the object selected
    entry = Appointment.objects.all()
    content = {'appointment': entry,
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_add_inspector.html',
        content,
        context_instance=RequestContext(request)
    )


def appointment_details(request):
    ''' appointment_details:  This is the detail view for each appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    entry = Appointment.objects.all()
    content = {'appointment': entry,
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_details.html',
        content,
        context_instance=RequestContext(request)
    )


def appointment_form(request):
    ''' appointment_form:  This is the user form for appointment entries

    Arguments:
        request
    Return:
        Page with form
    '''
    # TODO - Start adding the code
    pass
