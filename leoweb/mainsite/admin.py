# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models as m

# Register your models here.

class PositionAdmin(admin.ModelAdmin):
    list_display = ('x', 'y')
    
class DatarateAdmin(admin.ModelAdmin):
    list_display = ('dr',)

@admin.register(m.Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ("__str__", "started_at", "is_live")
    readonly_fields = ("hls_url",)    

admin.site.register(m.Position, PositionAdmin)
admin.site.register(m.Datarate, DatarateAdmin)