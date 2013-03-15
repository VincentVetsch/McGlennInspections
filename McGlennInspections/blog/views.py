from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Posts

sitename = "McGlenn Home Inspections"


def blog_page(request):
    '''
        This is the main view for all blog entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    # TODO - Order by date
    entries = Posts.objects.all()
    content = {'blog': entries, 'site': sitename}
    return render_to_response("blog.html", content, context_instance=RequestContext(request))


def blog_page_details(request):
    '''
        This is the detail view for each blog entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
