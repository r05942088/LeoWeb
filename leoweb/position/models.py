# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Position(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    
    class Meta:
        db_table="position"