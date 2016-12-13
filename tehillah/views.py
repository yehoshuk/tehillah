from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest, Http404
import datetime


def home(request):
    response = HttpRequest.get_full_path(request)
    return HttpResponse(response)


def dt(request):
    return HttpResponse(datetime.datetime.now())

def dt2(request):
    return render(request, 'current_datetime.html', {'current_date': datetime.datetime.now}) #parenthesis not used after now() in Context of Template


def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404
    #assert False
    return HttpResponse(datetime.datetime.now() + datetime.timedelta(hours=offset))
