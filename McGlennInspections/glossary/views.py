from django.core.paginator import InvalidPage, EmptyPage
from McGlennInspections.digg_paginator import DiggPaginator as Paginator
from django.shortcuts import render_to_response
from django.template import RequestContext
from glossary.models import Term
from django.contrib import admin
from McGlennInspections.settings import SITENAME
from navigation.models import get_navigation
admin.autodiscover()


def glossary_page(request):
    '''
        This is the main view for all glossary entries

        Arguments:
            request:
        Returns:
            Page with content values
    '''
    # DONE - Start adding the content to the page
    # DONE - Add pagination
    entries_list = Term.objects.order_by('title')
    paginator = Paginator(entries_list, 20)

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

    content = {'terms': entries,
               'navigation': get_navigation(),
               'site': SITENAME,
              }

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
