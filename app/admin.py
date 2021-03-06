# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Order, Approver, Status
# Register your models here.

class DisplayOrder(admin.ModelAdmin):
	list_display = ('name','mail','mobile','title','work','worktype','work','file','prof_name','prof_mail','approval1','approval2','approval3','completed','remarks1','remarks2','remarks3')

class DisplayApprover(admin.ModelAdmin):
	list_display = ('approver2','approver3')

class DisplayStatus(admin.ModelAdmin):
	list_display = ('order','status_text')

admin.site.register(Order, DisplayOrder)
admin.site.register(Approver, DisplayApprover)
admin.site.register(Status, DisplayStatus)