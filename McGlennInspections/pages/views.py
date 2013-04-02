from django.shortcuts import render_to_response
from django.template import RequestContext
from pages.models import HomePage
from McGlennInspections.settings import SITENAME
from navigation.models import get_navigation


def mcglenn(request):
    homepage = HomePage.objects.get(pk=1)
    context = {
        'homepage': homepage,
        'site': SITENAME,
        'navigation': get_navigation(),
    }
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request)
    )
