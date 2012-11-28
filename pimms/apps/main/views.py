from django.shortcuts import render_to_response 
from django.http import Http404
from django.template.context import RequestContext

from pimms.apps.helpers import genurls


def home(request):
    '''Controller for app home page
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
    
    return render_to_response('main/home.html', {'urls': urls},
                              context_instance=RequestContext(request))


def about(request):
    '''Controller for app about page
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
      
    return render_to_response('main/about.html', {'urls': urls},
                              context_instance=RequestContext(request))
