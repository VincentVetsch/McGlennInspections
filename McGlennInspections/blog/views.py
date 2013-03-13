from django.shortcuts import render_to_response
from blog.models import Posts


def blog(request):
    '''
        This is the view for blog
    '''
    return render_to_response("blog.html")
