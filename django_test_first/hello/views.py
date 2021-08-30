from django.urls import path
from . import views
from django.http import HttpResponse, HttpResponseRedirect

import logging

logger = logging.getLogger(__name__)


# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = """<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)


def sessfun(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del (request.session['num_visits'])
    resp = HttpResponse('view count=' + str(num_visits))
    resp.set_cookie('dj4e_cookie', '30f985ec', max_age=1000)
    return resp
