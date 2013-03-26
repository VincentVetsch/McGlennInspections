from django.shortcuts import render_to_response
from django.template import RequestContext
from appointment.models import Appointment, CustomerEmail, CustomerPhone
from McGlennInspections.settings import SITENAME
from django.contrib import admin
admin.autodiscover()


def accepted(thePost, theDataSet):
    '''accepted:  Performs manipulation on the appointment database.
        Arguments:
            request:        The POST request from Browser
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    theDataSet.accepted = [True, False][theDataSet.accepted == True]
    theDataSet.save()
    return True


def meeting(thePost, theDataSet):
    '''meeting:  Performs manipulation on the appointment database.
        Arguments:
            request:        The POST request from Browser
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.accepted:
        theDataSet.pre_aggrement_meeting = [True, False][theDataSet.pre_aggrement_meeting == True]
    theDataSet.save()
    return True


def report(thePost, theDataSet):
    '''report:  Performs manipulation on the appointment database.
        Arguments:
            request:        The POST request from Browser
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.pre_aggrement_meeting:
        theDataSet.report_completed = [True, False][theDataSet.report_completed == True]
    theDataSet.save()
    return True


def inspect(thePost, theDataSet):
    '''inspect:  Performs manipulation on the appointment database.
        Arguments:
            request:        The POST request from Browser
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.report_completed:
        theDataSet.inspection_completed = [True, False][theDataSet.inspection_completed == True]
    theDataSet.save()
    return True


def delete_record(thePost, theDataSet):
    '''delete_record:  Performs manipulation on the appointment database.
        Arguments:
            request:        The POST request from Browser
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    # TODO - Need to redirect to a confirmation window
    print 'Delete:  ' + thePost['delete']
    print theDataSet
    return True


def appointment(request):
    ''' appointment:  This is the main view for all appointment entries
        Arguments:
            request:        The POST request from Browser
        Returns: Page with content values
    '''
    # TODO - Insure that this page is only available to admin users
    # DONE - Start adding the content to the page
    # DONE - Refactor to function
    # This section of code retrieves the POST from template and changes the values
    # in the database
    entries = Appointment.objects.order_by('-date_requested').filter(report_completed=False)
    if request.method == 'POST':
        if ('accepted' in request.POST.keys()):
            f = 'accepted'
            accepted({f: request.POST[f]}, entries.get(pk=request.POST[f]))
        elif ('meeting' in request.POST.keys()):
            f = 'meeting'
            meeting({f: request.POST[f]}, entries.get(pk=request.POST[f]))
        elif ('inspection' in request.POST.keys()):
            f = 'inspection'
            inspect({f: request.POST[f]}, entries.get(pk=request.POST[f]))
        elif ('report' in request.POST.keys()):
            f = 'report'
            report({f: request.POST[f]}, entries.get(pk=request.POST[f]))
        elif ('delete' in request.POST.keys()):
            f = 'delete'
            delete_record({f: request.POST[f]}, entries.get(pk=request.POST[f]))

    # TODO - Add basic CustomerInformation
    content = {'appointment': entries,
               'site': SITENAME,
              }
    return render_to_response(
        "appointment.html",
        content,
        context_instance=RequestContext(request)
    )


# TODO - Delete this function
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


# TODO - Delete this function
def appointment_delete(request):
    ''' appointment_delete:  This is the view to Delete the appointment
        Arguments:
            request
        Return:
            Returns the render_to_response function
    '''
    # TODO - work on passing the object selected
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
