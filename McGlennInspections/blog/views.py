from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Posts
#This might not be proper but does work
from McGlennInspections.settings import SITENAME


def blog_page(request):
    '''
        blog_page: This is the main view for all blog entries

        Arguments:
             request
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    entries = Posts.objects.order_by('-timestamp')
    content = {'blog': entries, 'site': SITENAME}
    print content
    return render_to_response(
        "blog.html",
        content,
        context_instance=RequestContext(request)
    )


def blog_page_details(request):
    '''
        blog_page_details: This is the detail view for each blog entries

        Arguments:
             request
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass


def blog_comments(request):
    '''
        blog_comments:  This is a page for creating comments on blog entries.

        Arguments:
            request
        Return:
            render_to_response of page
    '''
    # TODO - Start adding the content to the page
    pass
