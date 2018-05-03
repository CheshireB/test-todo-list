from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'is_complete']


admin.site.register(Task, TaskAdmin)
