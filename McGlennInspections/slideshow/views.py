from django.shortcuts import render_to_response
from slideshow.models import Slide


def slideshow_page(request):
    '''
        This is the main view for all slideshow entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("slideshow.html", {'slideshow': Slide})


def slideshow_page_details(request):
    '''
        This is the detail view for each slideshow entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
