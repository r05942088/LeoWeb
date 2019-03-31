# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Position
from .serializers import PositionSerializer

from rest_framework import viewsets

# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer