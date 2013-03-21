from django.shortcuts import render_to_response
from django.template import RequestContext
from glossary.models import Term
from McGlennInspections.settings import SITENAME


def glossary_page(request):
    '''
        This is the main view for all glossary entries

        Arguments:
            request:
        Returns:
            Page with content values
    '''
    # DONE - Start adding the content to the page
    # TODO - Add pagination
    entries = Term.objects.order_by('-timestamp')
    content = {'term': entries, 'site': SITENAME}
    return render_to_response(
        "glossary.html",
        content,
        context_instance=RequestContext(request)
    )


def glossary_page_details(request):
    '''
        This is the detail view for each glossary entries

        Arguments:
            request:
        Returns:
            Page with details of the current term
    '''
    # TODO - Start adding the content to the page
    pass
