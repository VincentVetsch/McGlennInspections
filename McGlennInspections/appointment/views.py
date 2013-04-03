from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from appointment.models import Appointment, CustomerEmail, CustomerPhone
from appointment.forms import RegistrationForm
from McGlennInspections.settings import SITENAME
from django.contrib import admin
from datetime import date
from inspector.models import Inspector
from navigation.models import get_navigation
admin.autodiscover()


def accepted(theDataSet):
    '''accepted:  Performs manipulation on the appointment database.
        Arguments:
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    theDataSet.accepted = [True, False][theDataSet.accepted == True]
    if theDataSet.save():
        return True
    else:
        return False


def meeting(theDataSet):
    '''meeting:  Performs manipulation on the appointment database.
        Arguments:
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.accepted:
        theDataSet.pre_aggrement_meeting = [True, False][theDataSet.pre_aggrement_meeting == True]

    if theDataSet.save():
        return True
    else:
        return False


def inspect(theDataSet):
    '''inspect:  Performs manipulation on the appointment database.
        Arguments:
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.pre_aggrement_meeting:
        theDataSet.inspection_completed = [True, False][theDataSet.inspection_completed == True]
    if theDataSet.save():
        return True
    else:
        return False


def report(theDataSet):
    '''report:  Performs manipulation on the appointment database.
        Arguments:
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if theDataSet.inspection_completed:
        theDataSet.report_completed = [True, False][theDataSet.report_completed == True]
    if theDataSet.save():
        return True
    else:
        return False


def delete_record(theDataSet):
    '''delete_record:  Performs manipulation on the appointment database.
        Arguments:
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    # DONE - Need to redirect to a confirmation window
    theDataSet.remove = True
    if theDataSet.save():
        return True
    else:
        return False


def inspector(value, theDataSet):
    '''inspector:  Performs manipulation on the appointment database.
        Arguments:
            value:        The integer value from the POST
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    theDataSet.inspector_id = int(value)
    if theDataSet.save():
        return True
    else:
        return False


def add_inspector_note(value, theDataSet):
    '''add_inspector_note:  Performs manipulation on the appointment database.
        Arguments:
            value:          The integer value from the POST
            theDataSet:     The Data object from view
        Return:
            True if manipulation is complete.
    '''
    theDataSet.inspector_notes = value['add_inspector_note']
    if theDataSet.save():
        return True
    else:
        return False


def route_command(request, entries_list):
    '''route_command:  Performs manipulation on the appointment database.
        Arguments:
            request:        The integer value from the POST
            entries_list:   The Data object from view
        Return:
            True if manipulation is complete.
    '''
    if ('accepted' in request):
        accepted(entries_list)
        return True
    elif ('meeting' in request):
        meeting(entries_list)
        return True
    elif ('inspection' in request):
        inspect(entries_list)
        return True
    elif ('report' in request):
        report(entries_list)
        return True
    elif ('inspector_id' in request):
        inspector(request['inspector_id'], entries_list)
        return True
    elif ('delete' in request):
        delete_record(entries_list)
        return True
    elif ('add_inspector_note' in request):
        add_inspector_note(request, entries_list)
        return True
    else:
        return False


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
    entries_list = Appointment.objects.order_by('-date_requested', 'time_requested').filter(report_completed=False, remove=False)
    inspectors = Inspector.objects.exclude(slug='default-default')
    paginator = Paginator(entries_list, 5)

    if request.method == 'POST':
        entry = entries_list.get(pk=request.POST['app_id'])
        route_command(request.POST, entry)

    # Pagination
    # Get the page number
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    #Assign entries to paginator
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)

    content = {'appointment': entries,
               'inspectors': inspectors,
               'navigation': get_navigation(),
               'now': date.today(),
               'site': SITENAME,
              }
    return render_to_response(
        "appointment.html",
        content,
        context_instance=RequestContext(request)
    )


def appointment_completed(request):
    ''' appointment_complete:  This is the main view for all appointment entries
        Arguments:
            request:        The POST request from Browser
        Returns: Page with content values
    '''
    # TODO - Insure that this page is only available to admin users
    # DONE - Start adding the content to the page
    # DONE - Refactor to function
    # This section of code retrieves the POST from template and changes the values
    # in the database
    entries_list = Appointment.objects.order_by('-date_requested', 'time_requested').filter(report_completed=True, remove=False)
    inspectors = Inspector.objects.exclude(slug='default-default')
    paginator = Paginator(entries_list, 5)

    # Pagination
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    #Assign entries to paginator
    try:
        entries = paginator.page(page)
    except (EmptyPage, InvalidPage):
        entries = paginator.page(paginator.num_pages)

    content = {'appointment': entries,
               'inspectors': inspectors,
               'navigation': get_navigation(),
               'now': date.today(),
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


def change_inspector(request, appointment_slug):
    ''' change_inspector:  This is the view to add an inspector to the
        appointment.
        Arguments:
            request
        Return:
            Returns the render_to_response function
    '''
    # TODO - work on passing the object selected
    # TODO - Add a redirect
    entry = Appointment.objects.get(slug=appointment_slug)
    inspectors = Inspector.objects.exclude(slug='default-default')

    content = {'appointment': entry,
               'inspectors': inspectors,
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_add_inspector.html',
        content,
        context_instance=RequestContext(request)
    )


def inspector_notes(request, appointment_slug):
    ''' inspector_notes:  This is the view to add an inspector note to the
        appointment.
        Arguments:
            request
        Return:
            Returns the render_to_response function
    '''
    entry = Appointment.objects.get(slug=appointment_slug)

    content = {'note': entry,
               'site': SITENAME,
              }
    return render_to_response(
        'add_inspector_note.html',
        content,
        context_instance=RequestContext(request)
    )


def appointment_details(request, appointment_slug):
    ''' appointment_details:  This is the detail view for each appointment entries
        Arguments:
            request
        Returns: Page with content values
    '''
    # DONE - Start adding the content to the page
    entry = Appointment.objects.get(slug=appointment_slug)
    email = CustomerEmail.objects.filter(name=entry.pk)
    phone = CustomerPhone.objects.filter(name=entry.pk)
    if request.method == 'POST' and route_command(request.POST, entry):
        print "Success"

    content = {'detail': entry,
               'email': email,
               'phone': phone,
               'navigation': get_navigation(),
               'site': SITENAME,
              }
    return render_to_response(
        'appointment_details.html',
        content,
        context_instance=RequestContext(request)
    )


def customer_registration(request):
    '''
    '''
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        pass
    else:
        form = RegistrationForm()
        content = {'form': form}
        return render_to_response(
            'register.html',
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
