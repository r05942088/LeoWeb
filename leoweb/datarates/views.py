# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Datarate
from .serializers import DatarateSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DatarateViewSet(viewsets.ModelViewSet):
    queryset = Datarate.objects.all()
    serializer_class = DatarateSerializer
    # permission_classes = (IsAuthenticated,)