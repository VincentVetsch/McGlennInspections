from django.shortcuts import render_to_response
from blog.models import Posts


def blog_page(request):
    '''
        This is the view for blog
    '''
    # TODO - Start adding the content to the page
    return render_to_response("blog.html", {'blog': Posts})


def blog_page_details(request):
    pass
