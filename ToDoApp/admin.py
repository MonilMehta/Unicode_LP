from django.contrib import admin
from .models import *

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('taskname', 'date_created','task_completed') 
    search_fields = ("taskname",)
    
admin.site.register(Tasks,TasksAdmin)