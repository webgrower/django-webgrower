# -*- coding: utf-8 -*-
# import libraries for timezone
# for get a now time
from django.utils import timezone
# and function, which sends a request
# to web-browser
from django.http import HttpResponse

# def index has an argument named request
# request contains a few data, which helps
# us to get an URL or other data.
def index(request):
    # now, just return Response with some text
    return HttpResponse("Now: %s" % timezone.now())
