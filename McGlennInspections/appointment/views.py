from django.shortcuts import render_to_response
from django.template import RequestContext
from appointment.models import Appointment, CustomerInformation
from McGlennInspections.settings import SITENAME


def appointment_page(request):
    '''
        This is the main view for all appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Insure that this page is only available to admin users
    # TODO - Start adding the content to the page
    entries = Appointment.objects.order_by('-timestamp')
    apk = Appointment.objects.values()[0]['full_name_id']
    # TODO - Add basic CustomerInformation
    customer = CustomerInformation.objects.filter(id=apk)
    content = {'appointment': entries,
               'site': SITENAME,
               'customer': customer,
              }
    return render_to_response(
        "appointment.html",
        content,
        context_instance=RequestContext(request)
    )


def appointment_page_details(request):
    '''
        This is the detail view for each appointment entries

        Arguments:
            request
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
