from django.http import HttpResponse
from django.template import loader
import requests
import os

def index(request):
    # View code here...
    tmpl = loader.get_template('base.html.j2')
    try:
      upstream_url = "http://" + os.environ['UPSTREAM_ADDR'] + ":" + os.environ['UPSTREAM_PORT']
      r = requests.get(upstream_url, timeout=5)
    except requests.exceptions.RequestException as e:
      data = { 'json': [] }
    else:
      data = { 'json': r.json() }

    return HttpResponse(tmpl.render(data, request))
