from django.shortcuts import render_to_response
from django.template import RequestContext
from appointment.models import Appointment, CustomerEmail, CustomerPhone
from McGlennInspections.settings import SITENAME
from django.contrib import admin
admin.autodiscover()


def appointment(request):
    ''' appointment:  This is the main view for all appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Insure that this page is only available to admin users
    # TODO - Start adding the content to the page
    if request.method == 'POST':
        print request.POST

    entries = Appointment.objects.order_by('-date_requested')
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


def appointment_delete(request):
    ''' appointment_delete:  This is the view to Delete the appointment

        Arguments:
            request
        Return:
            Returns the render_to_response function
    '''
    # TODO - work on passing the object selected
    if request.method == 'POST':
        print request.POST
    content = {
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_delete.html',
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


def appointment_details(request, appointment_slug):
    ''' appointment_details:  This is the detail view for each appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    entry = Appointment.objects.get(slug=appointment_slug)
    email = CustomerEmail.objects.filter(name=entry.pk)
    phone = CustomerPhone.objects.filter(name=entry.pk)
    content = {'detail': entry,
               'email': email,
               'phone': phone,
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
