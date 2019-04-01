# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
def homepage(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)    