import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request


def index(request):
    now = datetime.datetime.now()
    ret = "<html><body>Agora é: %s</body></html>" % now
    return HttpResponse(ret)
