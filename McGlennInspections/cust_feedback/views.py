from django.shortcuts import render_to_response
from cust_feedback.models import Feedback


def cust_feedback_page(request):
    '''
        This is the main view for all cust_feedback entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    return render_to_response("cust_feedback.html", {'cust_feedback': Feedback})


def cust_feedback_page_details(request):
    '''
        This is the detail view for each appointment entries
        Returns: Page with content values
    '''
    # TODO - Start adding the content to the page
    pass
