from django.shortcuts import render_to_response
from glossary.models import Terms
from McGlennInspections.settings import SITENAME


def glossary_page(request):
    '''
        This is the main view for all glossary entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("glossary.html", {'terms': Terms})


def glossary_page_details(request):
    '''
        This is the detail view for each glossary entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
