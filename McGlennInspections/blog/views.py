from django.shortcuts import render_to_response
from blog.models import Posts


def blog_page(request):
    '''
        This is the main view for all blog entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("blog.html", {'blog': Posts})


def blog_page_details(request):
    '''
        This is the detail view for each blog entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
