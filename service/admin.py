from django.contrib import admin
from service.models import task
from django.db import models
# Register your models here.
class serviceadmin(admin.ModelAdmin):
    list_display = ('task_reason','task_step','created_date')

admin.site.register(task,serviceadmin)