from django.shortcuts import render_to_response
from rvalues.models import RValue


def rvalues_page(request):
    '''
        This is the main view for all rvalue entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("rvalues.html", {'rvalues': RValue})


def rvalues_page_details(request):
    '''
        This is the detail view for each rvalue entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
