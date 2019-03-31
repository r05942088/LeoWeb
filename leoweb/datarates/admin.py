# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Datarate

# Register your models here.
class DatarateAdmin(admin.ModelAdmin):
    list_display = ('dr',)
    
admin.site.register(Datarate, DatarateAdmin)