# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.template.loader import get_template
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import models

# Create your views here.
def homepage(request):
    position = models.Position.objects.all()[0]
    datarate = models.Datarate.objects.all()[0]
    response = "position: {} {}".format(position.x,position.y)
    template = get_template('base.html')
    html = template.render()
    
    return HttpResponse(html)
    
@require_POST
@csrf_exempt
def start_stream(request):
    """ This view is called when a stream starts.
    """
    stream = get_object_or_404(Stream, key=request.POST["name"])

    # Ban streamers by setting them inactive
    if not stream.user.is_active:
        return HttpResponseForbidden("Inactive user")

    # Don't allow the same stream to be published multiple times
    if stream.started_at:
        return HttpResponseForbidden("Already streaming")

    stream.started_at = timezone.now()
    stream.save()

    # Redirect to the streamer's public username
    return redirect(stream.user.username)


@require_POST
@csrf_exempt
def stop_stream(request):
    """ This view is called when a stream stops.
    """
    Stream.objects.filter(key=request.POST["name"]).update(started_at=None)
    return HttpResponse("OK")